# ec2-imagebuilder-samples

This repository contains examples for demo-ing EC2 Image Builder

## Local development

EC2 Image Builder uses [AWSTOE](https://docs.aws.amazon.com/imagebuilder/latest/userguide/image-builder-component-manager-local.html) to execute documents. 

A few important switches to know are:

- `-t | --trace` this will dump logs to the console.
- `-d | --documents` to specify the path to your document(s).
- `-h | --help` 

Usage:

```ps
.\awstoe.exe validate -d c:\path\to\document.yml
.\awstoe.exe run -t -d c:\path\to\document.yml
```