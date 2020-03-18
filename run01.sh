$ bazel run //cmd/apply:apply -- --config_path=./instance_config.yaml --terraform_configs_dir=tmp/dpt_output

# //cmd is the cmd folder in the healthacare deploy
# config_path=./instance_config.yaml is the file I created under deploy/samples/instance_templates 
# this command is executed under healthcare/deploy/samples/instance_templates folder where we haev our yaml templates.
