---
layout: default
title: PRiSM: An Agentic Multimodal Benchmark for Scientific Reasoning via Python-Grounded Evaluation
---

# PRiSM: An Agentic Multimodal Benchmark for Scientific Reasoning via Python-Grounded Evaluation

**arXiv**: [2512.05930v1](https://arxiv.org/abs/2512.05930) | [PDF](https://arxiv.org/pdf/2512.05930.pdf)

**作者**: Shima Imani, Seungwhan Moon, Adel Ahmadyan, Lu Zhang, Kirmani Ahmed, Babak Damavandi

---

## 💡 一句话要点

**提出PRiSM基准以通过Python代码评估科学推理能力**

**关键词**: `科学推理评估` `多模态基准` `Python代码生成` `动态问题生成` `视觉语言模型`

## 📋 核心要点

1. 现有基准在科学领域评估中缺乏动态性和中间推理步骤
2. PRiSM利用PrismAgent生成动态多模态问题，包含可执行Python代码作为真值
3. 通过五个评估任务揭示视觉语言模型在科学推理中的局限性

## 📄 摘要（原文）

> Evaluating vision-language models (VLMs) in scientific domains like mathematics and physics poses unique challenges that go far beyond predicting final answers. These domains demand conceptual understanding, symbolic reasoning, and adherence to formal laws, requirements that most existing benchmarks fail to address. In particular, current datasets tend to be static, lacking intermediate reasoning steps, robustness to variations, or mechanisms for verifying scientific correctness. To address these limitations, we introduce PRiSM, a synthetic, fully dynamic, and multimodal benchmark for evaluating scientific reasoning via grounded Python code. PRiSM includes over 24,750 university-level physics and math problems, and it leverages our scalable agent-based pipeline, PrismAgent, to generate well-structured problem instances. Each problem contains dynamic textual and visual input, a generated figure, alongside rich structured outputs: executable Python code for ground truth generation and verification, and detailed step-by-step reasoning. The dynamic nature and Python-powered automated ground truth generation of our benchmark allow for fine-grained experimental auditing of multimodal VLMs, revealing failure modes, uncertainty behaviors, and limitations in scientific reasoning. To this end, we propose five targeted evaluation tasks covering generalization, symbolic program synthesis, perturbation robustness, reasoning correction, and ambiguity resolution. Through comprehensive evaluation of existing VLMs, we highlight their limitations and showcase how PRiSM enables deeper insights into their scientific reasoning capabilities.

