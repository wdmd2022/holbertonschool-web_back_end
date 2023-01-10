export default function createEmployeesObject(departmentName, employees) {
  const llCoolObj = {
    [departmentName]:
      employees,
  };
  return llCoolObj;
}
