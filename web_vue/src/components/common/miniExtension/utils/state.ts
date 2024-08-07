/**
 * 状态变化
 *
 */
class SateSet {
  set: Set<unknown>

  constructor() {
    this.set = new Set()
  }
  /**
   * 新状态
   * @param newSet
   */
  setNew<K>(newSet: Set<K>) {
    const oldSet = this.set
    const tempSet = new Set(newSet)
    // 剩下的是添加的
    newSet.forEach((e) => {
      if (this.set.has(e)) {
        newSet.delete(e)
        oldSet.delete(e)
      }
    })
    this.set = tempSet

    return {
      add: newSet,
      delete: oldSet as Set<K>
    }
  }
  addSets<K>(addSet: Set<K>) {
    addSet.forEach((e) => this.set.add(e))
  }
  deleteSets<K>(deleteSet: Set<K>) {
    deleteSet.forEach((e) => this.set.delete(e))
  }
  clear() {
    this.set.clear()
  }
}

export { SateSet }
