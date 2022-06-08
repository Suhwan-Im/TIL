<template>
  <div>
    <ul>
      <li v-for="(todo, idx) in tododata" :key="`todo-${idx}`">
        <span :class="{ completed: todo.completed }" @click='toggleTodo(todo)'>{{ todo.item }}</span>
        <i class="fa-solid fa-delete-left removeIcon" @click="removeTodo(todo, idx)"></i>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    tododata: Array,
  },
  methods: {
    removeTodo(todo, idx) {
      this.$emit('removeTodo', todo.item, idx)
    },
    toggleTodo(idx) {
      this.$emit('toggleTodo',idx)
    }
  },
}
</script>

<style>
  li {
    display: flex;
    height: 30px;
  }

  .removeIcon {
    color: rgb(220, 53, 31);
    margin-left: auto;
  }

  .completed {
    text-decoration: line-through;
    color: gray;
  }
</style>