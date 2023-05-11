export default function createReportObject(employeesList) {
  const reporty = {
    allEmployees: employeesList,
    getNumberOfDepartments() {
      return Object.keys(employeesList).length;
    },
  };
  return reporty;
}
