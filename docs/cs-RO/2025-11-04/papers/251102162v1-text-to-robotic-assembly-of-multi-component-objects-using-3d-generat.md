---
layout: default
title: Text to Robotic Assembly of Multi Component Objects using 3D Generative AI and Vision Language Models
---

# Text to Robotic Assembly of Multi Component Objects using 3D Generative AI and Vision Language Models

**arXiv**: [2511.02162v1](https://arxiv.org/abs/2511.02162) | [PDF](https://arxiv.org/pdf/2511.02162.pdf)

**作者**: Alexander Htet Kyaw, Richa Gupta, Dhruv Shah, Anoop Sinha, Kory Mathewson, Stefanie Pender, Sachin Chitta, Yotto Koga, Faez Ahmed, Lawrence Sass, Randall Davis

---

## 💡 一句话要点

**提出集成3D生成AI与视觉语言模型的管道，实现多组件对象的机器人组装**

**关键词**: `3D生成AI` `视觉语言模型` `机器人组装` `多组件对象` `零样本推理` `人机交互`

## 📋 核心要点

1. 核心问题：3D生成AI难以创建涉及多组件类型的物理对象
2. 方法要点：利用视觉语言模型进行零样本多模态推理，分解AI生成网格为多组件3D模型
3. 实验或效果：用户偏好VLM生成分配达90.6%，优于规则和随机方法

## 📄 摘要（原文）

> Advances in 3D generative AI have enabled the creation of physical objects
> from text prompts, but challenges remain in creating objects involving multiple
> component types. We present a pipeline that integrates 3D generative AI with
> vision-language models (VLMs) to enable the robotic assembly of multi-component
> objects from natural language. Our method leverages VLMs for zero-shot,
> multi-modal reasoning about geometry and functionality to decompose
> AI-generated meshes into multi-component 3D models using predefined structural
> and panel components. We demonstrate that a VLM is capable of determining which
> mesh regions need panel components in addition to structural components, based
> on object functionality. Evaluation across test objects shows that users
> preferred the VLM-generated assignments 90.6% of the time, compared to 59.4%
> for rule-based and 2.5% for random assignment. Lastly, the system allows users
> to refine component assignments through conversational feedback, enabling
> greater human control and agency in making physical objects with generative AI
> and robotics.

