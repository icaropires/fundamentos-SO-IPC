# Host A folder.
HOST_A := @cd ./host_a/

# Host B folder.
HOST_B := @cd ./host_b/

# Middleware A folder.
MIDDLEWARE_A := @cd ./middleware_a/

# Middleware B folder.
MIDDLEWARE_B := @cd ./middleware_b/

# Compile project. 
all: build_host_a build_host_b build_middleware_a build_middleware_b

# Compile each project.
build_host_a:
	$(HOST_A) && make

build_host_b:
	$(HOST_B) && make

build_middleware_a:
	$(MIDDLEWARE_A) && make

build_middleware_b:
	$(MIDDLEWARE_B) && make

run_host_a:
	$(HOST_A) && ./bin/host_a

run_host_b:
	$(HOST_B) && ./bin/host_b

run_middleware_a:
	$(MIDDLEWARE_A) && ./bin/middleware_a

run_middleware_b:
	$(MIDDLEWARE_B) && ./bin/middleware_b

clean:
	@rm -rf */obj/* */bin/*
