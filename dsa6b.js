// ================================================================================
// PRACTICAL 6B: DATA SYSTEM FOR ANALYTICS (DSA)
// TOPIC: MONGODB INDEXING & QUERY OPTIMIZATION (.explain("executionStats"))
// ENVIRONMENT: MONGODB SHELL (mongosh)
// ================================================================================
// FULL QUESTIONS:
// Q. Demonstrate Index Management and Performance Optimization:
//    1. View existing indexes using getIndexes().
//    2. Drop an existing index using dropIndex().
//    3. Query without an index and analyze executionStats (stage: COLLSCAN, totalDocsExamined).
//    4. Create a Single-Field Index using createIndex({ desg: 1 }) and observe performance gains.
//    5. Create a Multi-Field (Compound) Index using createIndex({ dept: 1, desg: 1 }) 
//       and observe pinpoint query execution (totalDocsExamined: 1).
// ================================================================================

use abdulwahab;

// --------------------------------------------------------------------------------
// 1. INSPECT AND DROP EXISTING INDEXES
// --------------------------------------------------------------------------------
// Check current indexes on employee collection
db.employee.getIndexes();

// Drop compound index if previously created
db.employee.dropIndex('dept_1_desg_1');

// Verify default primary key (_id_) index remains
db.employee.getIndexes();


// --------------------------------------------------------------------------------
// 2. QUERY WITHOUT INDEX (BASELINE PERFORMANCE BENCHMARK)
// --------------------------------------------------------------------------------
// Find employees whose designation is 'Member'
db.employee.find({ desg: 'Member' });

// Analyze query planner and execution metrics before index creation
db.employee.find({ desg: 'Member' }).explain('executionStats');
// === OBSERVATION ===
// winningPlan.stage : 'COLLSCAN' (Collection Scan - examines every document)
// totalDocsExamined : 10 (Full scan overhead)


// --------------------------------------------------------------------------------
// 3. SINGLE-FIELD INDEXING
// --------------------------------------------------------------------------------
// Create an index on the 'desg' field (1 for ascending)
db.employee.createIndex({ desg: 1 });

// Re-run explain plan on the same query to observe performance improvement
db.employee.find({ desg: 'Member' }).explain('executionStats');
// === OBSERVATION ===
// winningPlan.stage : 'FETCH' with 'IXSCAN' (Index Scan)
// totalDocsExamined : 4 (Significantly reduced docs examined!)


// --------------------------------------------------------------------------------
// 4. MULTI-FIELD (COMPOUND) INDEXING
// --------------------------------------------------------------------------------
// Create compound index across both 'dept' and 'desg' fields
db.employee.createIndex({ dept: 1, desg: 1 });

// Verify new compound index 'dept_1_desg_1' exists in collection
db.employee.getIndexes();

// Execute multi-attribute query and analyze execution statistics
db.employee.find({ dept: 'Acc', desg: 'Member' }).explain('executionStats');
// === OBSERVATION ===
// winningPlan.stage : 'FETCH'
// totalKeysExamined : 1
// totalDocsExamined : 1 (Pinpoint accuracy - only examined matching document!)
