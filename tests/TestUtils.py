def assert_comparison(case, actual, expected, tolerance):
    if isinstance(actual, float) and isinstance(expected, float):
        case.assertAlmostEqual(actual, expected, delta=tolerance)