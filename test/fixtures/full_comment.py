"""
@api post /incidents/
description: >-
 a multiline
 description
parameters:
    - in: query
      name: nice
      description: wow
      schema:
        type: integer
    - in: query
      name: great
      description: cool
      schema:
        type: string
responses:
    "200":
        description: A success msg
        content:
            application/json:
                schema:
                    $ref: '#/components/schemas/Thing'
    "400":
        description: A failure msg
        content:
            text/plain:
                schema:
                    $ref: '#/components/schemas/Test'
"""