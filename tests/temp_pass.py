'1: val_to_eval = ${module.child.myoutput}'
'[8 -(instance_type)-> 0]'
val_to_eval=${module.child.myoutput}, replaced_key=module.child.myoutput, str(evaluated_attribute_value)=bar
'2: val_to_eval = bar'
'[8 -(instance_type)-> 6]'
'1: val_to_eval = ${local.x.y}'
'[14 -(default)-> 3]'
val_to_eval=${local.x.y}, replaced_key=local.x.y, str(evaluated_attribute_value)=z
'2: val_to_eval = z'
'1: val_to_eval = ${local.is_vpc}'
'[10 -(vpc)-> 5]'
val_to_eval=${local.is_vpc}, replaced_key=local.is_vpc, str(evaluated_attribute_value)=True
'2: val_to_eval = True'
'1: val_to_eval = ${var.bucket_name}'
'[1 -(bucket_name)-> 12]'
val_to_eval=${var.bucket_name}, replaced_key=var.bucket_name, str(evaluated_attribute_value)={'val': 'MyBucket'}
'2: val_to_eval = {'val':'MyBucket'}'
'1: val_to_eval = ${var.region}'
'[9 -(region)-> 15]'
val_to_eval=${var.region}, replaced_key=var.region, str(evaluated_attribute_value)=us-west-2
'2: val_to_eval = us-west-2'
'1: val_to_eval = ${var.aws_profile}'
'[7 -(profile)-> 16]'
val_to_eval=${var.aws_profile}, replaced_key=var.aws_profile, str(evaluated_attribute_value)=default
'2: val_to_eval = default'
'1: val_to_eval = ${format(\"-%s\",var.dummy_1)}'
'[2 -(dummy_with_dash)-> 17]'
val_to_eval=${format(\"-%s\",var.dummy_1)}, replaced_key=var.dummy_1, str(evaluated_attribute_value)=dummy_1
'2: val_to_eval = ${format(\"-%s\",dummy_1)}'
'1: val_to_eval = ${local.bucket_name}'
'[9 -(bucket)-> 1]'
val_to_eval=${local.bucket_name}, replaced_key=local.bucket_name, str(evaluated_attribute_value)={'val': 'MyBucket'}
'2: val_to_eval = {'val':'MyBucket'}'
'1: val_to_eval = ${local.dummy_with_dash}'
'[4 -(ami_name)-> 2]'
val_to_eval=${local.dummy_with_dash}, replaced_key=local.dummy_with_dash, str(evaluated_attribute_value)=${format(\"-%s\",dummy_1)}
'2: val_to_eval = ${format(\"-%s\",dummy_1)}'
'1: val_to_eval = ${aws.east1}'
'1: val_to_eval = ${var.acl_default_value}'
'[13 -(default)-> 14]'
val_to_eval=${var.acl_default_value}, replaced_key=var.acl_default_value, str(evaluated_attribute_value)=z
'2: val_to_eval = z'
'1: val_to_eval = ${aws_instance.example.id}'
'[10 -(instance)-> 8]'
'1: val_to_eval = ${aws_s3_bucket.template_bucket.acl}'
'[11 -(value)-> 9]'
val_to_eval=${aws_s3_bucket.template_bucket.acl}, replaced_key=aws_s3_bucket.template_bucket.acl, str(evaluated_attribute_value)=${var.acl}
'2: val_to_eval = ${var.acl}'
'1: val_to_eval = ${local.ami_name}'
'[8 -(ami)-> 4]'
val_to_eval=${local.ami_name}, replaced_key=local.ami_name, str(evaluated_attribute_value)=${format(\"-%s\",dummy_1)}
'2: val_to_eval = ${format(\"-%s\",dummy_1)}'
'1: val_to_eval = ${var.acl}'
'[9 -(acl)-> 13]'
val_to_eval=${var.acl}, replaced_key=var.acl, str(evaluated_attribute_value)=z
'2: val_to_eval = z'
'1: val_to_eval = ${var.acl}'
'[11 -(value)-> 9]'
val_to_eval=${var.acl}, replaced_key=aws_s3_bucket.template_bucket.acl, str(evaluated_attribute_value)=z
'2: val_to_eval = aws_s3_bucket.template_bucket.acl'
'1: val_to_eval = ${aws_instance.example.id}'
'[10 -(instance)-> 8]'
'1: val_to_eval = aws_s3_bucket.template_bucket.acl'
'[11 -(value)-> 9]'
val_to_eval=aws_s3_bucket.template_bucket.acl, replaced_key=aws_s3_bucket.template_bucket.acl, str(evaluated_attribute_value)=z
'2: val_to_eval = z'