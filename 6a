// ================================================================================
// PRACTICAL 6A: DATA SYSTEM FOR ANALYTICS (DSA)
// TOPIC: MONGODB CRUD OPERATIONS, OPERATORS & AGGREGATION PIPELINE
// ENVIRONMENT: MONGODB SHELL (mongosh)
// ================================================================================
// FULL QUESTIONS:
// Q. Open Command Prompt, run 'mongosh', and execute:
//    1. Create database 'abdulwahab' and collection 'employees'.
//    2. Perform single (insertOne) and multiple (insertMany) document insertions.
//    3. Retrieve all documents and specific documents with field projections.
//    4. Perform document updates using updateOne and $set.
//    5. Apply Relational ($lte) and Arithmetic ($inc) operators.
//    6. Delete documents matching criteria using deleteOne.
//    7. Demonstrate Logical Operators ($and, $not, $or, $nor, $exists, $in, $nin).
//    8. Construct Aggregation Pipelines using $match, $group, $sort, $limit, $project.
// ================================================================================

// --------------------------------------------------------------------------------
// 1. DATABASE & COLLECTION SETUP
// --------------------------------------------------------------------------------
// Show all available databases
show dbs;

// Switch to database
use abdulwahab;

// Create 'employees' collection
db.createCollection("employees");

// Verify created collection
show collections;


// --------------------------------------------------------------------------------
// 2. INSERT OPERATIONS (insertOne & insertMany)
// --------------------------------------------------------------------------------
// Insert first single document
db.employees.insertOne({
    name: "Alice", 
    age: 21
});

// Insert second single document with full profile
db.employees.insertOne({
    name: "John", 
    age: 25, 
    desgn: "Professor", 
    dept: "BDA", 
    salary: 12000.00, 
    email: ["john2@gmail.com", "john33@gmail.com"], 
    doj: "2012-06-01"
});

// Insert multiple documents (Batch 1)
db.employees.insertMany([
    {
        name: "Mary", 
        age: 27, 
        desgn: "HOD", 
        dept: "BDA", 
        salary: 20000.00, 
        doj: "2011-04-01"
    },
    {
        name: "Bob", 
        age: 24, 
        desgn: "AS", 
        dept: "BVoc SD", 
        salary: 15000.00, 
        email: ["bo123@gmail.com"], 
        doj: "2014-08-01"
    }
]);

// Insert multiple documents (Batch 2)
db.employees.insertMany([
    {
        name: "Andrew", 
        age: 25, 
        desgn: "HOD", 
        dept: "BVoc SD", 
        salary: 23000.00, 
        email: ["andrewgriffin.2@gmail.com", "andrew.griffin@gmail.com"], 
        doj: "2011-06-01"
    },
    {
        name: "Sara", 
        age: 30, 
        desgn: "Professor", 
        dept: "BSc IT", 
        salary: 14000.00, 
        email: ["sara@gmail.com"], 
        doj: "2015-04-01"
    }
]);


// --------------------------------------------------------------------------------
// 3. READ & QUERY OPERATIONS
// --------------------------------------------------------------------------------
// Find all documents
db.employees.find();

// Find document with filter
db.employees.find({ name: "Bob" });

// Find document with field projection (return only name and desgn)
db.employees.find({ name: "Bob" }, { desgn: 1, name: 1 });


// --------------------------------------------------------------------------------
// 4. UPDATE OPERATIONS
// --------------------------------------------------------------------------------
// Update salary for employee 'Sara'
db.employees.updateOne({ name: "Sara" }, { $set: { salary: 15000 } });
db.employees.find({ name: "Sara" });

// Update multiple fields for 'Bob'
db.employees.updateOne({ name: "Bob" }, { $set: { salary: 18000, desgn: "HOD" } });
db.employees.find({ name: "Bob" });

// Update designation and salary for 'John'
db.employees.updateOne({ name: "John" }, { $set: { salary: 30000, desgn: "Expert" } });
db.employees.find({ name: "John" });


// --------------------------------------------------------------------------------
// 5. RELATIONAL & ARITHMETIC OPERATORS
// --------------------------------------------------------------------------------
// Relational Operator ($lte: less than or equal)
db.employees.find(
    { salary: { $lte: 20000 } }, 
    { name: 1, desgn: 1, salary: 1 }
);

// Arithmetic Increment Operator ($inc: increase salary by 10000 for non-Bob employees)
db.employees.updateMany(
    { name: { $ne: "Bob" } }, 
    { $inc: { salary: 10000 } }
);


// --------------------------------------------------------------------------------
// 6. DELETE OPERATION
// --------------------------------------------------------------------------------
// Delete employee with designation 'Expert'
db.employees.deleteOne({ desgn: { $eq: "Expert" } });
db.employees.find({ desgn: "Expert" });


// --------------------------------------------------------------------------------
// 7. LOGICAL OPERATORS
// --------------------------------------------------------------------------------
// $and Operator
db.employees.find({
    $and: [
        { name: "Mary" }, 
        { desgn: "HOD" }
    ]
});

// $not Operator
db.employees.find({
    name: { $not: { $eq: "Sara" } }
});

// $or Operator
db.employees.find({
    $or: [
        { age: { $gt: 25 } }, 
        { desgn: "HOD" }
    ]
});

// $nor Operator
db.employees.find({
    $nor: [
        { age: 25 }, 
        { desgn: "HOD" }
    ]
});

// $exists Operator (check if document contains field 'email')
db.employees.find({
    email: { $exists: true }
});

// Display employees whose salary are exactly 35000 or 25000 using $or
db.employees.find({
    $or: [
        { salary: 35000 }, 
        { salary: 25000 }
    ]
});

// Using $in Operator
db.employees.find({
    salary: { $in: [18000, 35000] }
});

// Using $nin (Not in) Operator
db.employees.find({
    salary: { $nin: [25000, 35000] }
});


// --------------------------------------------------------------------------------
// 8. AGGREGATION PIPELINE ($match, $group, $sort, $limit, $project)
// --------------------------------------------------------------------------------

// Aggregation 1: $match - Filter by department
db.employees.aggregate([
    { $match: { dept: "BSc IT" } }
]);

// Aggregation 2: $group - Calculate average & total salary per department
db.employees.aggregate([
    { 
        $group: {
            _id: "$dept",
            avgSalary: { $avg: "$salary" },
            totalSalary: { $sum: "$salary" }
        }
    }
]);

// Aggregation 3: $sort - Sort by salary descending (-1)
db.employees.aggregate([
    { $sort: { salary: -1 } }
]);

// Aggregation 4: $limit - Find top highest paid employees
db.employees.aggregate([
    { $sort: { salary: -1 } },
    { $limit: 2 }
]);

// Aggregation 5: $project - Reshape output fields (exclude _id, include name, dept, salary)
db.employees.aggregate([
    { 
        $project: { 
            _id: 0, 
            name: 1, 
            dept: 1, 
            salary: 1 
        } 
    }
]);
