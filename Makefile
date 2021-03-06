clean:
	rm -rf build build.zip
	rm -rf __pycache__
	find . -name "*.pyc" -exec rm -f {} \;

fetch-dependencies:
	mkdir -p bin/

	# Get chromedriver
	curl -SL https://chromedriver.storage.googleapis.com/2.32/chromedriver_linux64.zip > chromedriver.zip
	unzip chromedriver.zip -d bin/

	# Get Headless-chrome
	curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-29/stable-headless-chromium-amazonlinux-2017-03.zip > headless-chromium.zip
	unzip headless-chromium.zip -d bin/

	# Clean
	rm headless-chromium.zip chromedriver.zip

docker-build:
	docker-compose build

docker-run:
	docker-compose run lambda src.lambda.lambda_handler

build-lambda-package: clean
	mkdir build
	cp -r src build/.
	cp -r bin build/.
	cp -r lib build/.
	pip install -r requirements.txt -t build/lib/.
	cd build; zip -9qr build.zip .
	cp build/build.zip .
	rm -rf build

upload-lambda: build-lambda-package
	aws s3 cp build.zip s3://lambda-sender/build.zip
