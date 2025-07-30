
# Task Overview

A SaaS marketing platform is onboarding a growing number of new users. The business requires each user to receive a welcome email immediately after a successful signup, but it's critical that the email operation does not slow down the user registration API or risk blocking other incoming requests. Currently, users experience delayed or missing welcome emails, and some registration calls are slow or time out. This inconsistency affects user onboarding experience and overall platform performance.

## Guidance

- Use FastAPI's recommended background task pattern for side-effect operations like email sending
- Ensure API responsiveness by not waiting on the email-sending function to finish before returning the registration response
- Maintain clean project structure: separate concerns for models, database interactions, and background task logic
- Validate user data with Pydantic models and use async I/O correctly for non-blocking code paths
- The background task function should be robust and not block the event loop; consider how it is invoked and defined
- Pay attention to proper error responses and logging for troubleshooting background and request-related issues

## Objectives

- Refactor the user registration endpoint so that sending a welcome email occurs as a background process
- Guarantee the API returns the registration response quickly, regardless of the email operation
- Adhere to async programming patterns for both request handling and background work
- Ensure that the email functionality can be extended or monitored for debugging
- Validate that only successful registrations attempt to trigger the background task

## How to Verify

- Register a new user and observe that the API responds quickly, even if the email task takes longer
- Confirm that the welcome email task is executed outside the main response lifecycle
- Trigger several concurrent registrations and observe stable, non-blocking behavior
- Validate that registrations without errors initiate the background email logic
- Review application logs or instrumentation to confirm that email-sending operations do not block the request or slow down throughput
