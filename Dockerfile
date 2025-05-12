FROM public.ecr.aws/lambda/python:3.13

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT} 
COPY requirements.txt  ${LAMBDA_TASK_ROOT} 
COPY mongodb-enterprise-8.0.repo /etc/yum.repos.d/mongodb-enterprise-8.0.repo
# install dependencies
#RUN yum install -y mongodb-atlas
RUN dnf -y install mongodb-atlas
#RUN curl -O https://fastdl.mongodb.org/mongocli/mongodb-atlas-cli_1.41.2_linux_x86_64.tar.gz
#RUN tar -zxvf mongodb-atlas-cli_1.41.2_linux_x86_64.tar.gz
#RUN cp mongodb-atlas-cli_1.41.2_linux_x86_64/bin/atlas /usr/local/bin/atlas
RUN atlas
RUN locate atlas
RUN ls -l /usr/local/bin/atlas


RUN pip3 install --user -r requirements.txt
# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.lambda_handler" ]
