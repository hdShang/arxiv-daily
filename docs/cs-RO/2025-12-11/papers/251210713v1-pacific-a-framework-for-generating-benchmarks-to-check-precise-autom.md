---
layout: default
title: PACIFIC: a framework for generating benchmarks to check Precise Automatically Checked Instruction Following In Code
---

# PACIFIC: a framework for generating benchmarks to check Precise Automatically Checked Instruction Following In Code

**arXiv**: [2512.10713v1](https://arxiv.org/abs/2512.10713) | [PDF](https://arxiv.org/pdf/2512.10713.pdf)

**作者**: Itay Dreyfuss, Antonio Abu Nassar, Samuel Ackerman, Axel Ben David, Rami Katan, Orna Raz, Marcel Zalmanovici

---

## 💡 一句话要点

**提出PACIFIC框架以自动生成基准测试，评估大语言模型在代码任务中的指令遵循和代码干运行能力。**

**关键词**: `大语言模型评估` `代码干运行` `指令遵循` `基准测试生成` `代码助手` `训练数据污染`

## 📋 核心要点

1. 核心问题：大语言模型代码助手需准确遵循用户指令，现有方法常依赖工具或代理行为，难以隔离评估其内在推理能力。
2. 方法要点：PACIFIC框架自动生成基准测试变体，控制难度，通过简单输出比较评估指令遵循和代码干运行能力，减少训练数据污染。
3. 实验或效果：生成多难度基准测试，评估多个先进模型，结果显示PACIFIC能有效区分模型能力，提供可扩展、抗污染的方法。

## 📄 摘要（原文）

> Large Language Model (LLM)-based code assistants have emerged as a powerful application of generative AI, demonstrating impressive capabilities in code generation and comprehension. A key requirement for these systems is their ability to accurately follow user instructions. We present Precise Automatically Checked Instruction Following In Code (PACIFIC), a novel framework designed to automatically generate benchmarks that rigorously assess sequential instruction-following and code dry-running capabilities in LLMs, while allowing control over benchmark difficulty. PACIFIC produces benchmark variants with clearly defined expected outputs, enabling straightforward and reliable evaluation through simple output comparisons. In contrast to existing approaches that often rely on tool usage or agentic behavior, our work isolates and evaluates the LLM's intrinsic ability to reason through code behavior step-by-step without execution (dry running) and to follow instructions. Furthermore, our framework mitigates training data contamination by facilitating effortless generation of novel benchmark variations. We validate our framework by generating a suite of benchmarks spanning a range of difficulty levels and evaluating multiple state-of-the-art LLMs. Our results demonstrate that PACIFIC can produce increasingly challenging benchmarks that effectively differentiate instruction-following and dry running capabilities, even among advanced models. Overall, our framework offers a scalable, contamination-resilient methodology for assessing core competencies of LLMs in code-related tasks.

