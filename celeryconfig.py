# global Celery options that apply to all configurations

# Specify the serializer to use for task messages.
# By default, Celery uses JSON, which is a lightweight and widely supported
# format, but may not be suitable for all use cases. In this case, we use
# the pickle serializer, which can handle more complex Python objects.
task_serializer = "pickle"
# Specify the serializer to use for task results.
# By default, Celery uses JSON to serialize task results, but this may not be
# suitable for all use cases, as JSON has limitations when it comes to
# serializing complex data structures and types. In this case, we use the
# pickle serializer for consistency with the task serializer.
result_serializer = "pickle"
# Specify the content types that the worker is willing to accept.
# This is a security measure that helps protect against deserialization
# attacks, which can occur when a malicious user sends a specially crafted
# message to a worker. By default, Celery accepts a range of content types,
# but we restrict it to the pickle serializer only to reduce the attack surface.
accept_content = ["pickle"]
# Specify a list of modules to import when starting the worker.
# This is necessary to ensure that the worker has access to the task functions
# that it needs to execute. It's best practice to specify the full import path
# to the module to avoid potential naming conflicts or ambiguity. Note that
# this option should only be used to import modules that define tasks, and not
# for general-purpose imports or global variables.
imports = ["uaf.device_farming.device_tasks"]
# Specify the maximum number of retries for a failed task.
# In this case, we set the max retries to 3, which means that Celery will attempt to execute
# the task up to 3 times before marking it as failed.
task_max_retries = 1
# Specify the delay between retries for a failed task.
# In this case, we set the retry delay to 5 seconds, which means that Celery will wait 5 seconds
# between each retry attempt.
task_retry_delay = 3
# Specify the concurrency settings for the worker pool.
# By default, Celery uses a single worker process with a concurrency of 1, which may not be sufficient
# for high-load environments. In this case, we set the concurrency to 4, which means that the worker
# will create 1 worker processes to handle tasks concurrently.
worker_concurrency = 1
# Specify the maximum number of tasks that a worker can execute before being recycled.
# This setting can help prevent memory leaks and ensure that workers are periodically restarted
# to free up system resources. In this case, we set the worker max tasks per child to 1000.
worker_max_tasks_per_child = 1000
