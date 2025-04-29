FROM public.ecr.aws/lambda/python:3.13

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT} 
COPY requirements.txt  ${LAMBDA_TASK_ROOT} 

# install dependencies
RUN pip3 install --user -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.lambda_handler" ]
