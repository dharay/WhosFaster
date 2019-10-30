import XCTest

#if !canImport(ObjectiveC)
public func allTests() -> [XCTestCaseEntry] {
    return [
        testCase(Kitura_SwiftTests.allTests),
    ]
}
#endif
