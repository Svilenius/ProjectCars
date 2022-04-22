def __str__(self):
    return '\t'.jpin(str(x) for x in [self._producer, self._model, self._year, self._colour, self._kilometers])