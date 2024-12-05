#!/bin/bash
export DB_URL='postgresql://student:student@localhost:5432/casting_agency'
export DB_TEST_URL='postgresql://student:student@localhost:5432/casting_agency_test'
export AUTH0_DOMAIN='dev-w8yi3jize45h8fgh.us.auth0.com'
export ALGORITHMS='RS256'
export API_AUDIENCE='casting-agency'
export EXCITED="true"

# Tokens
export ASSISTANT='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJPSjR2dVlRQnMtZHZ0WWE4UndPRiJ9.eyJpc3MiOiJodHRwczovL2Rldi13OHlpM2ppemU0NWg4ZmdoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzQ3MmQ0OWFlNmU0NDI1ZThlOGZlMmMiLCJhdWQiOiJjYXN0aW5nLWFnZW5jeSIsImlhdCI6MTczMzM2NjExMywiZXhwIjoxNzMzNDUyNTEzLCJzY29wZSI6IiIsImF6cCI6Im1hNTVDdGR5TFdYeXBROGExTmprb1ZYTkluMWxicGgzIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.imjPQQHwMeVAshOC17CxdfE3wqkJS3vXCjASZPq3_GTTaujhPTOZ_WOjI7pJJC7kyRvQpC4oJ8r53k3txCfEd6X-PcI9rU3XBEGc4aVqbAHAa1hYv9gQDbS-eQfIjDYpzT-ERqfaL5vcqP67ThzRsjCzuWOasNJNpvzW28sFkFe7LrYLkwdNtRlDwCRfZgsHG4yr0TmAPOufuiyslhjiE0JFe4KIBV9ykQdT4D6sxaVX_JV1ENo-FCq9htX_O62u0kYJarxFDB8IbZ7qxPe01vv0qcxGYMg1SlO3dPnq-CX0ghlmbOMOWkSVng6dQaDV2782nDQbNpXYHBUptSTQEA'
export DIRECTOR='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJPSjR2dVlRQnMtZHZ0WWE4UndPRiJ9.eyJpc3MiOiJodHRwczovL2Rldi13OHlpM2ppemU0NWg4ZmdoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzUwOTc2Y2E2NzEzN2YwMmU1MTE3MzkiLCJhdWQiOiJjYXN0aW5nLWFnZW5jeSIsImlhdCI6MTczMzM2NjIzMCwiZXhwIjoxNzMzNDUyNjMwLCJzY29wZSI6IiIsImF6cCI6Im1hNTVDdGR5TFdYeXBROGExTmprb1ZYTkluMWxicGgzIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.iQ-Tp5eVPbvaijLCvE_vXhSXWvAWZR7hX1sJi6E7lULFb4Hz1dR4P3eBHhac4DO_1b7v-E8A405wZAm2tOILfujjmSnmXcVQRbep7GHOncaMxfMv2XzUw9yPBQqyPf06uTYc5F33swwSQrvKfudYE6fQo-nQJOvOJ84JU-PgSsSZ9rstNzA6p1RvGLuC5G_Q0oJWivFlZJxEAvLrOSq2GUqJOOMdxvlIZ67dctkTFyKV9pWYbsFOYb2IG96y4sdx9-K4iSdNwO1UWsabrFbnZlcS4OIQNKUeVD5hol_QKc98dSu3prgrKBqktvkLO0WsnPuGoyEC8-5M2cg9_Xr9_A'
export PRODUCER='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImJPSjR2dVlRQnMtZHZ0WWE4UndPRiJ9.eyJpc3MiOiJodHRwczovL2Rldi13OHlpM2ppemU0NWg4ZmdoLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NzQxZDQ2MmNkZjUxNWM2ODA2YWQzNDciLCJhdWQiOiJjYXN0aW5nLWFnZW5jeSIsImlhdCI6MTczMzM2NTk0NCwiZXhwIjoxNzMzNDUyMzQ0LCJzY29wZSI6IiIsImF6cCI6Im1hNTVDdGR5TFdYeXBROGExTmprb1ZYTkluMWxicGgzIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.LdFb1TtPqH5dNNUfUk1QXL4Ek1dp37l7b0lZd9U4vkSALhKfuhcLuvpVCB1uAa64RspFkFInEGrMZ8FkLbX5KWlJOuCbfzbyg8EEsgvofvW9M93IRF-lrQmKiGCFqb63TwuiKUeYyTlV3CuFf5ZMBnceYY6yS8b4ZWgAGvzPI4cm3e0X7rFLw3vXtuCVBe-IIEJT0WPPMYdAUO1pAR2TswJ8QoAfLgdtT3msfqLK6dBYx27hpMWOKDfk-7d_6JdfEjlVuXfKGzlO8zqCKl-PqAlLT3B_AhAMC5PdPbA_C9OxlDBJkuuSznTwoSvJWB4X4l0Nvm5rhwx8ID8a1B6mVQ'
echo "setup.sh script executed successfully!"