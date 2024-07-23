// vite.config.ts
import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "file:///D:/github/geogpu/code-template/web_vue/node_modules/.pnpm/vite@5.3.3_@types+node@20.14.10/node_modules/vite/dist/node/index.js";
import vue from "file:///D:/github/geogpu/code-template/web_vue/node_modules/.pnpm/@vitejs+plugin-vue@5.0.5_vite@5.3.3_@types+node@20.14.10__vue@3.4.31_typescript@5.4.5_/node_modules/@vitejs/plugin-vue/dist/index.mjs";
import VueDevTools from "file:///D:/github/geogpu/code-template/web_vue/node_modules/.pnpm/vite-plugin-vue-devtools@7.3.5_rollup@4.18.1_vite@5.3.3_@types+node@20.14.10__vue@3.4.31_typescript@5.4.5_/node_modules/vite-plugin-vue-devtools/dist/vite.mjs";
import UnoCSS from "file:///D:/github/geogpu/code-template/web_vue/node_modules/.pnpm/unocss@0.60.4_postcss@8.4.39_rollup@4.18.1_vite@5.3.3_@types+node@20.14.10_/node_modules/unocss/dist/vite.mjs";
import AutoImport from "file:///D:/github/geogpu/code-template/web_vue/node_modules/.pnpm/unplugin-auto-import@0.17.6_@vueuse+core@10.11.0_vue@3.4.31_typescript@5.4.5___rollup@4.18.1/node_modules/unplugin-auto-import/dist/vite.js";
import Components from "file:///D:/github/geogpu/code-template/web_vue/node_modules/.pnpm/unplugin-vue-components@0.27.2_@babel+parser@7.24.7_rollup@4.18.1_vue@3.4.31_typescript@5.4.5_/node_modules/unplugin-vue-components/dist/vite.js";
import Icons from "file:///D:/github/geogpu/code-template/web_vue/node_modules/.pnpm/unplugin-icons@0.19.0_@vue+compiler-sfc@3.4.31_vue-template-compiler@2.7.16/node_modules/unplugin-icons/dist/vite.js";
import IconsResolver from "file:///D:/github/geogpu/code-template/web_vue/node_modules/.pnpm/unplugin-icons@0.19.0_@vue+compiler-sfc@3.4.31_vue-template-compiler@2.7.16/node_modules/unplugin-icons/dist/resolver.js";
import path from "path";
var __vite_injected_original_dirname = "D:\\github\\geogpu\\code-template\\web_vue";
var __vite_injected_original_import_meta_url = "file:///D:/github/geogpu/code-template/web_vue/vite.config.ts";
var pathSrc = path.resolve(__vite_injected_original_dirname, "src");
var vite_config_default = defineConfig({
  plugins: [
    vue(),
    VueDevTools(),
    UnoCSS(),
    AutoImport({
      // 自动导入 Vue 相关函数，如：ref, reactive, toRef 等
      imports: ["vue", "vue-router", "pinia"],
      resolvers: [
        // 自动导入图标组件
        IconsResolver({ prefix: "Icon" })
      ],
      dts: path.resolve(pathSrc, "auto-imports.d.ts")
    }),
    Components({
      resolvers: [
        // 自动注册图标组件  edit引入格式 <i-ep-edit />
        IconsResolver({ enabledCollections: ["ep"] })
      ],
      dts: path.resolve(pathSrc, "components.d.ts")
    }),
    // 自动引入图标资源
    Icons({ autoInstall: true })
  ],
  // 路径别名
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", __vite_injected_original_import_meta_url))
    }
  },
  // 开发服务设置
  server: {
    port: 1666,
    strictPort: true,
    host: "0.0.0.0",
    headers: {
      "Access-Control-Allow-Origin": "*"
    }
  }
});
export {
  vite_config_default as default
};
//# sourceMappingURL=data:application/json;base64,ewogICJ2ZXJzaW9uIjogMywKICAic291cmNlcyI6IFsidml0ZS5jb25maWcudHMiXSwKICAic291cmNlc0NvbnRlbnQiOiBbImNvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9kaXJuYW1lID0gXCJEOlxcXFxnaXRodWJcXFxcZ2VvZ3B1XFxcXGNvZGUtdGVtcGxhdGVcXFxcd2ViX3Z1ZVwiO2NvbnN0IF9fdml0ZV9pbmplY3RlZF9vcmlnaW5hbF9maWxlbmFtZSA9IFwiRDpcXFxcZ2l0aHViXFxcXGdlb2dwdVxcXFxjb2RlLXRlbXBsYXRlXFxcXHdlYl92dWVcXFxcdml0ZS5jb25maWcudHNcIjtjb25zdCBfX3ZpdGVfaW5qZWN0ZWRfb3JpZ2luYWxfaW1wb3J0X21ldGFfdXJsID0gXCJmaWxlOi8vL0Q6L2dpdGh1Yi9nZW9ncHUvY29kZS10ZW1wbGF0ZS93ZWJfdnVlL3ZpdGUuY29uZmlnLnRzXCI7aW1wb3J0IHsgZmlsZVVSTFRvUGF0aCwgVVJMIH0gZnJvbSAnbm9kZTp1cmwnXHJcblxyXG5pbXBvcnQgeyBkZWZpbmVDb25maWcgfSBmcm9tICd2aXRlJ1xyXG5pbXBvcnQgdnVlIGZyb20gJ0B2aXRlanMvcGx1Z2luLXZ1ZSdcclxuaW1wb3J0IFZ1ZURldlRvb2xzIGZyb20gJ3ZpdGUtcGx1Z2luLXZ1ZS1kZXZ0b29scydcclxuXHJcbi8vIGNzcyBcdThGODVcdTUyQTlcclxuaW1wb3J0IFVub0NTUyBmcm9tICd1bm9jc3Mvdml0ZSdcclxuXHJcbi8vIFx1ODFFQVx1NTJBOFx1NUJGQ1x1NTE2NVx1NjMwOVx1OTcwMFx1NUYxNVx1NTE2NSB2dWUgaW9uXHJcbmltcG9ydCBBdXRvSW1wb3J0IGZyb20gJ3VucGx1Z2luLWF1dG8taW1wb3J0L3ZpdGUnXHJcbmltcG9ydCBDb21wb25lbnRzIGZyb20gJ3VucGx1Z2luLXZ1ZS1jb21wb25lbnRzL3ZpdGUnXHJcbmltcG9ydCBJY29ucyBmcm9tICd1bnBsdWdpbi1pY29ucy92aXRlJ1xyXG5pbXBvcnQgSWNvbnNSZXNvbHZlciBmcm9tICd1bnBsdWdpbi1pY29ucy9yZXNvbHZlcidcclxuaW1wb3J0IHBhdGggZnJvbSAncGF0aCdcclxuY29uc3QgcGF0aFNyYyA9IHBhdGgucmVzb2x2ZShfX2Rpcm5hbWUsICdzcmMnKVxyXG5cclxuLy8gaHR0cHM6Ly92aXRlanMuZGV2L2NvbmZpZy9cclxuZXhwb3J0IGRlZmF1bHQgZGVmaW5lQ29uZmlnKHtcclxuICBwbHVnaW5zOiBbXHJcbiAgICB2dWUoKSxcclxuICAgIFZ1ZURldlRvb2xzKCksXHJcbiAgICBVbm9DU1MoKSxcclxuICAgIEF1dG9JbXBvcnQoe1xyXG4gICAgICAvLyBcdTgxRUFcdTUyQThcdTVCRkNcdTUxNjUgVnVlIFx1NzZGOFx1NTE3M1x1NTFGRFx1NjU3MFx1RkYwQ1x1NTk4Mlx1RkYxQXJlZiwgcmVhY3RpdmUsIHRvUmVmIFx1N0I0OVxyXG4gICAgICBpbXBvcnRzOiBbJ3Z1ZScsICd2dWUtcm91dGVyJywgJ3BpbmlhJ10sXHJcbiAgICAgIHJlc29sdmVyczogW1xyXG4gICAgICAgIC8vIFx1ODFFQVx1NTJBOFx1NUJGQ1x1NTE2NVx1NTZGRVx1NjgwN1x1N0VDNFx1NEVGNlxyXG4gICAgICAgIEljb25zUmVzb2x2ZXIoeyBwcmVmaXg6ICdJY29uJyB9KVxyXG4gICAgICBdLFxyXG4gICAgICBkdHM6IHBhdGgucmVzb2x2ZShwYXRoU3JjLCAnYXV0by1pbXBvcnRzLmQudHMnKVxyXG4gICAgfSksXHJcbiAgICBDb21wb25lbnRzKHtcclxuICAgICAgcmVzb2x2ZXJzOiBbXHJcbiAgICAgICAgLy8gXHU4MUVBXHU1MkE4XHU2Q0U4XHU1MThDXHU1NkZFXHU2ODA3XHU3RUM0XHU0RUY2ICBlZGl0XHU1RjE1XHU1MTY1XHU2ODNDXHU1RjBGIDxpLWVwLWVkaXQgLz5cclxuICAgICAgICBJY29uc1Jlc29sdmVyKHsgZW5hYmxlZENvbGxlY3Rpb25zOiBbJ2VwJ10gfSlcclxuICAgICAgXSxcclxuICAgICAgZHRzOiBwYXRoLnJlc29sdmUocGF0aFNyYywgJ2NvbXBvbmVudHMuZC50cycpXHJcbiAgICB9KSxcclxuICAgIC8vIFx1ODFFQVx1NTJBOFx1NUYxNVx1NTE2NVx1NTZGRVx1NjgwN1x1OEQ0NFx1NkU5MFxyXG4gICAgSWNvbnMoeyBhdXRvSW5zdGFsbDogdHJ1ZSB9KVxyXG4gIF0sXHJcbiAgLy8gXHU4REVGXHU1Rjg0XHU1MjJCXHU1NDBEXHJcbiAgcmVzb2x2ZToge1xyXG4gICAgYWxpYXM6IHtcclxuICAgICAgJ0AnOiBmaWxlVVJMVG9QYXRoKG5ldyBVUkwoJy4vc3JjJywgaW1wb3J0Lm1ldGEudXJsKSlcclxuICAgIH1cclxuICB9LFxyXG4gIC8vIFx1NUYwMFx1NTNEMVx1NjcwRFx1NTJBMVx1OEJCRVx1N0Y2RVxyXG4gIHNlcnZlcjoge1xyXG4gICAgcG9ydDogMTY2NixcclxuICAgIHN0cmljdFBvcnQ6IHRydWUsXHJcbiAgICBob3N0OiAnMC4wLjAuMCcsXHJcbiAgICBoZWFkZXJzOiB7XHJcbiAgICAgICdBY2Nlc3MtQ29udHJvbC1BbGxvdy1PcmlnaW4nOiAnKidcclxuICAgIH1cclxuICB9XHJcbn0pXHJcbiJdLAogICJtYXBwaW5ncyI6ICI7QUFBOFMsU0FBUyxlQUFlLFdBQVc7QUFFalYsU0FBUyxvQkFBb0I7QUFDN0IsT0FBTyxTQUFTO0FBQ2hCLE9BQU8saUJBQWlCO0FBR3hCLE9BQU8sWUFBWTtBQUduQixPQUFPLGdCQUFnQjtBQUN2QixPQUFPLGdCQUFnQjtBQUN2QixPQUFPLFdBQVc7QUFDbEIsT0FBTyxtQkFBbUI7QUFDMUIsT0FBTyxVQUFVO0FBZGpCLElBQU0sbUNBQW1DO0FBQW9KLElBQU0sMkNBQTJDO0FBZTlPLElBQU0sVUFBVSxLQUFLLFFBQVEsa0NBQVcsS0FBSztBQUc3QyxJQUFPLHNCQUFRLGFBQWE7QUFBQSxFQUMxQixTQUFTO0FBQUEsSUFDUCxJQUFJO0FBQUEsSUFDSixZQUFZO0FBQUEsSUFDWixPQUFPO0FBQUEsSUFDUCxXQUFXO0FBQUE7QUFBQSxNQUVULFNBQVMsQ0FBQyxPQUFPLGNBQWMsT0FBTztBQUFBLE1BQ3RDLFdBQVc7QUFBQTtBQUFBLFFBRVQsY0FBYyxFQUFFLFFBQVEsT0FBTyxDQUFDO0FBQUEsTUFDbEM7QUFBQSxNQUNBLEtBQUssS0FBSyxRQUFRLFNBQVMsbUJBQW1CO0FBQUEsSUFDaEQsQ0FBQztBQUFBLElBQ0QsV0FBVztBQUFBLE1BQ1QsV0FBVztBQUFBO0FBQUEsUUFFVCxjQUFjLEVBQUUsb0JBQW9CLENBQUMsSUFBSSxFQUFFLENBQUM7QUFBQSxNQUM5QztBQUFBLE1BQ0EsS0FBSyxLQUFLLFFBQVEsU0FBUyxpQkFBaUI7QUFBQSxJQUM5QyxDQUFDO0FBQUE7QUFBQSxJQUVELE1BQU0sRUFBRSxhQUFhLEtBQUssQ0FBQztBQUFBLEVBQzdCO0FBQUE7QUFBQSxFQUVBLFNBQVM7QUFBQSxJQUNQLE9BQU87QUFBQSxNQUNMLEtBQUssY0FBYyxJQUFJLElBQUksU0FBUyx3Q0FBZSxDQUFDO0FBQUEsSUFDdEQ7QUFBQSxFQUNGO0FBQUE7QUFBQSxFQUVBLFFBQVE7QUFBQSxJQUNOLE1BQU07QUFBQSxJQUNOLFlBQVk7QUFBQSxJQUNaLE1BQU07QUFBQSxJQUNOLFNBQVM7QUFBQSxNQUNQLCtCQUErQjtBQUFBLElBQ2pDO0FBQUEsRUFDRjtBQUNGLENBQUM7IiwKICAibmFtZXMiOiBbXQp9Cg==
