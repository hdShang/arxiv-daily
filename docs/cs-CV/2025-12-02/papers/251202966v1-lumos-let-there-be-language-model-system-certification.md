---
layout: default
title: Lumos: Let there be Language Model System Certification
---

# Lumos: Let there be Language Model System Certification

**arXiv**: [2512.02966v1](https://arxiv.org/abs/2512.02966) | [PDF](https://arxiv.org/pdf/2512.02966.pdf)

**作者**: Isha Chaudhary, Vedaant Jain, Avaljot Singh, Kavya Sachdeva, Sayan Ranu, Gagandeep Singh

---

## 💡 一句话要点

**提出Lumos框架以系统化指定和形式化认证语言模型系统行为**

**关键词**: `语言模型系统认证` `概率编程语言` `形式化验证` `视觉语言模型` `自动驾驶安全` `提示分布`

## 📋 核心要点

1. 核心问题：缺乏语言模型系统行为的系统化指定和形式化认证框架
2. 方法要点：基于图的命令式概率编程DSL，支持通过统计认证器验证任意提示分布
3. 实验或效果：在自动驾驶场景中，发现Qwen-VL在雨天右转时存在至少90%概率的安全失败

## 📄 摘要（原文）

> We introduce the first principled framework, Lumos, for specifying and formally certifying Language Model System (LMS) behaviors. Lumos is an imperative probabilistic programming DSL over graphs, with constructs to generate independent and identically distributed prompts for LMS. It offers a structured view of prompt distributions via graphs, forming random prompts from sampled subgraphs. Lumos supports certifying LMS for arbitrary prompt distributions via integration with statistical certifiers. We provide hybrid (operational and denotational) semantics for Lumos, providing a rigorous way to interpret the specifications. Using only a small set of composable constructs, Lumos can encode existing LMS specifications, including complex relational and temporal specifications. It also facilitates specifying new properties - we present the first safety specifications for vision-language models (VLMs) in autonomous driving scenarios developed with Lumos. Using these, we show that the state-of-the-art VLM Qwen-VL exhibits critical safety failures, producing incorrect and unsafe responses with at least 90% probability in right-turn scenarios under rainy driving conditions, revealing substantial safety risks. Lumos's modular structure allows easy modification of the specifications, enabling LMS certification to stay abreast with the rapidly evolving threat landscape. We further demonstrate that specification programs written in Lumos enable finding specific failure cases exhibited by state-of-the-art LMS. Lumos is the first systematic and extensible language-based framework for specifying and certifying LMS behaviors, paving the way for a wider adoption of LMS certification.

