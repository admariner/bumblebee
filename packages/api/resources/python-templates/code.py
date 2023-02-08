#{this.measureTime ? this.timeStart : ""}
_output = None
res = {'result': _output}
#{this.measureTime ? this.timeEnd : ""}
#{this.includeVariables}
#{this.outputJSON("res")}