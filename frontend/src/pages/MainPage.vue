<template>
  <div class="h1 ">
    {{ title }}
  </div>
</template>

<script lang="ts">
    import { defineComponent } from "vue";
    import {useUserStore} from "../store/user";

    export default defineComponent({
        data() {
            return {
                title: "Main Page",
            }
        },
    })
</script>