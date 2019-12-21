---
layout: "post"
category: "OpenGL"
date: 2019-10-25

---

### 

```c++
vertexSStream << vertexFile.rdbuf();
fragmentSStream << fragmentFile.rdbuf();

vertexString = vertexSStream.str();
fragmentString = fragmentSStream.str();

vertexSource = vertexString.c_str()
fragmentSource = fragmentString.c_str()

vertext = glCreateShader(GL_VERTEX_SHADER);
glShaerSource(vertex, 1, &vertexSource, NULL);
glCompileShader(vertex);

fragment = glCreateShader(GL_FRAGMENT_SHADER);
glShaderSource(fragment, 1, &fragmentSource, NULL);
glCompileShader(fragment);

ID = glCreateProgram();
glAttachShader(ID, vertex);
glAttachShader(ID, fragment);
glLinkProgram(ID);
glDeleteShader(vertex);
glDeleteShader(fragment);

void Shader::user(){
  glUerProgram(ID);
}
```

