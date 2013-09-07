"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": "I---like--python",
            "answer": "I-like-python"
        },
        {
            "input": "No-double--dashes",
            "answer": "No-double-dashes"
        },
        {
            "input": "normal-text-with-single-dashes",
            "answer": "normal-text-with-single-dashes"
        },
        {
            "input": "triple---dashes---is---not---good",
            "answer": "triple-dashes-is-not-good"
        },
        {
            "input": "One-Two--Three---Four----Five-----Six",
            "answer": "One-Two-Three-Four-Five-Six"
        }
    ],
    "Extra": [
        {
            "input": "a-b--c",
            "answer": "a-b-c"
        },
        {
            "input": "a-a-a-a",
            "answer": "a-a-a-a"
        },
        {
            "input": "b---b----b",
            "answer": "b-b-b"
        },
        {
            "input": "a-b--c-d--e",
            "answer": "a-b-c-d-e"
        },
        {
            "input": "123--------321",
            "answer": "123-321"
        }
    ]
}
