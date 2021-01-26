FROM alpine:latest 

RUN apk add python3 py3-pip --no-cache \
&& apk add graphviz \
&& apk add git
COPY . .
RUN pip install -r requirements.txt
CMD [ "python3", "./test.py","url.json"] 
