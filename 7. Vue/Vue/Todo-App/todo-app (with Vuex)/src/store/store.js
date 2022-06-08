import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const storage = {
  fetch() {
    const todos = []
    if(localStorage.length > 0) {
      for(var i = 0; i < localStorage.length; i++) {
        const todoItem = localStorage.getItem( localStorage.key(i) ) 
        todos.push(JSON.parse(todoItem))
      }
    }
    return todos
  }
}

export const store = new Vuex.Store({
  state: {
    headerText: 'My Todo List',
    todos: storage.fetch(),
  },
  mutations: {
    addTodo(state, item) {
      const todoObj = {
        item: item,
        completed: false,
      }
      localStorage.setItem(item, JSON.stringify(todoObj))
      state.todos.push(todoObj)
    },
    removeTodo(state, payload) {
      localStorage.removeItem(payload.todoItem)
      state.todos.splice(payload.idx, 1)
    },
    toggleTodo(state, idx) {
      state.todos[idx].completed = !state.todos[idx].completed

      localStorage.removeItem(state.todos[idx].item)
      localStorage.setItem(state.todos[idx].item, JSON.stringify(state.todos[idx]))
    },
    clearAll(state) {
      localStorage.clear()
      state.todos = []
    }
  }
})