---
layout: default
title: SymPyBench: A Dynamic Benchmark for Scientific Reasoning with Executable Python Code
---

# SymPyBench: A Dynamic Benchmark for Scientific Reasoning with Executable Python Code

**arXiv**: [2512.05954v1](https://arxiv.org/abs/2512.05954) | [PDF](https://arxiv.org/pdf/2512.05954.pdf)

**作者**: Shima Imani, Seungwhan Moon, Adel Ahmadyan, Lu Zhang, Kirmani Ahmed, Babak Damavandi

---

## 💡 一句话要点

**提出SymPyBench动态基准，以评估语言模型在科学推理中的表现**

**关键词**: `科学推理基准` `动态评估` `可执行代码` `物理问题` `语言模型评估` `参数化问题`

## 📋 核心要点

1. 核心问题：缺乏大规模、参数化的科学推理基准，难以全面评估模型能力
2. 方法要点：构建包含15,045个物理问题的基准，支持无限输入配置，提供结构化推理和可执行代码
3. 实验或效果：引入新评估指标，测试先进语言模型，揭示科学推理的优缺点

## 📄 摘要（原文）

> We introduce, a large-scale synthetic benchmark of 15,045 university-level physics problems (90/10% train/test split). Each problem is fully parameterized, supporting an effectively infinite range of input configurations, and is accompanied by structured, step-by-step reasoning and executable Python code that produces the ground-truth solution for any parameter set. The benchmark contains three question types: MC-Symbolic (multiple-choice with symbolic options), MC-Numerical (multiple-choice with numerical options), and free-form (open-ended responses). These diverse formats test complementary reasoning skills. By leveraging the dynamic, code-driven nature of the benchmark, we introduce three novel evaluation metrics in addition to standard accuracy: Consistency Score, Failure Rate, and Confusion Rate, that quantify variability and uncertainty across problem variants. Experiments with state-of-the-art instruction-tuned language models reveal both strengths and limitations in scientific reasoning, positioning SymPyBench as a foundation for developing more robust and interpretable reasoning systems

