from copy import deepcopy
from typing import List, Optional

from checkov.terraform.graph_builder.graph_components.block_types import BlockType
from checkov.terraform.graph_builder.graph_components.blocks import Block, get_inner_attributes


class Module:
    def __init__(self, source_dir, encode):
        self.path = ''
        self.blocks: List[Block] = []
        self.customer_name = ''
        self.account_id = ''
        self.source = ''
        self.resources_types = set()
        self.source_dir = source_dir
        self.encode = encode

    def add_blocks(self, block_type, blocks, path, source, dependencies: Optional[List[List[str]]]=None):
        self.source = source
        if dependencies is None:
            dependencies = [[]]
        if self._block_type_to_func.get(block_type):
            self._block_type_to_func[block_type].__call__(self, blocks, path, dependencies)

    def _add_to_blocks(self, block: Block, dependencies: List[List[str]]):
        for dep_trail in dependencies:
            block = deepcopy(block)
            block.module_dependency = '->'.join(dep_trail)
            self.blocks.append(block)

    def _add_provider(self, blocks, path, dependencies):
        for provider_dict in blocks:
            for name in provider_dict:
                attributes = provider_dict[name]
                provider_name = name
                if attributes.get('alias'):
                    provider_name = f"{provider_name}.{attributes.get('alias')[0]}"
                provider_block = Block(
                    block_type=BlockType.PROVIDER,
                    name=provider_name,
                    config=provider_dict,
                    path=path,
                    attributes=attributes,
                    source=self.source,
                    encode=self.encode
                )
                self._add_to_blocks(provider_block, dependencies)

    def _add_variable(self, blocks, path, dependencies):
        for variable_dict in blocks:
            for name in variable_dict:
                attributes = variable_dict[name]
                variable_block = Block(
                    block_type=BlockType.VARIABLE,
                    name=name,
                    config=variable_dict,
                    path=path,
                    attributes=attributes,
                    source=self.source,
                    encode=self.encode
                )
                self._add_to_blocks(variable_block, dependencies)

    def _add_locals(self, blocks, path, dependencies):
        for blocks_section in blocks:
            for name in blocks_section:
                local_block = Block(
                    block_type=BlockType.LOCALS,
                    name=name,
                    config={name: blocks_section[name]},
                    path=path,
                    attributes={name: blocks_section[name]},
                    source=self.source,
                    encode=self.encode
                )
                self._add_to_blocks(local_block, dependencies)

    def _add_output(self, blocks, path, dependencies):
        for output_dict in blocks:
            for name in output_dict:
                if type(output_dict[name]) is not dict:
                    continue
                output_block = Block(
                    block_type=BlockType.OUTPUT,
                    name=name,
                    config=output_dict,
                    path=path,
                    attributes={'value': output_dict[name].get('value')},
                    source=self.source,
                    encode=self.encode
                )
                self._add_to_blocks(output_block, dependencies)

    def _add_module(self, blocks, path, dependencies):
        for module_dict in blocks:
            for name in module_dict:
                module_block = Block(
                    block_type=BlockType.MODULE,
                    name=name,
                    config=module_dict,
                    path=path,
                    attributes=module_dict[name],
                    source=self.source,
                    encode=self.encode
                )
                self._add_to_blocks(module_block, dependencies)

    def _add_resource(self, blocks, path, dependencies):
        for resource_dict in blocks:
            for resource_type in resource_dict:
                self.resources_types.add(resource_type)
                for name in resource_dict[resource_type]:
                    attributes = deepcopy(resource_dict[resource_type][name])
                    provisioner = attributes.get('provisioner')
                    if provisioner is not None:
                        self._handle_provisioner(provisioner, attributes)
                    attributes['resource_type'] = [resource_type]
                    resource_block = Block(
                        block_type=BlockType.RESOURCE,
                        name=resource_type + '.' + name,
                        config=resource_dict,
                        path=path,
                        attributes=attributes,
                        id=resource_type + '.' + name,
                        source=self.source,
                        encode=self.encode
                    )
                    self._add_to_blocks(resource_block, dependencies)

    def _add_data(self, blocks, path, dependencies):
        for data_dict in blocks:
            for data_type in data_dict:
                for name in data_dict[data_type]:
                    data_block = Block(
                        block_type=BlockType.DATA,
                        name=data_type + '.' + name,
                        config=data_dict,
                        path=path,
                        attributes=data_dict.get(data_type, {}).get(name, {}),
                        id=data_type + '.' + name,
                        source=self.source,
                        encode=self.encode
                    )
                    self._add_to_blocks(data_block, dependencies)

    def _add_terraform_block(self, blocks, path, dependencies):
        for terraform_dict in blocks:
            for name in terraform_dict:
                terraform_block = Block(
                    block_type=BlockType.TERRAFORM,
                    name=name,
                    config=terraform_dict,
                    path=path,
                    attributes={},
                    source=self.source,
                    encode=self.encode
                )
                self._add_to_blocks(terraform_block, dependencies)

    def _add_tf_var(self, blocks, path, dependencies):
        for tf_var_name, attributes in blocks.items():
            tfvar_block = Block(
                block_type=BlockType.TF_VARIABLE,
                name=tf_var_name,
                config={tf_var_name: attributes},
                path=path,
                attributes=attributes,
                source=self.source,
                encode=self.encode
            )
            self._add_to_blocks(tfvar_block, dependencies)

    @staticmethod
    def _handle_provisioner(provisioner, attributes):
        for pro in provisioner:
            if pro.get('local-exec'):
                inner_attributes = get_inner_attributes('provisioner/local-exec', pro['local-exec'])
                attributes.update(inner_attributes)
            elif pro.get('remote-exec'):
                inner_attributes = get_inner_attributes('provisioner/remote-exec', pro['remote-exec'])
                attributes.update(inner_attributes)
        attributes.pop('provisioner')

    def get_resources_types(self):
        return list(self.resources_types)

    _block_type_to_func = {
        BlockType.DATA: _add_data,
        BlockType.LOCALS: _add_locals,
        BlockType.MODULE: _add_module,
        BlockType.OUTPUT: _add_output,
        BlockType.PROVIDER: _add_provider,
        BlockType.RESOURCE: _add_resource,
        BlockType.TERRAFORM: _add_terraform_block,
        BlockType.TF_VARIABLE: _add_tf_var,
        BlockType.VARIABLE: _add_variable,
    }
