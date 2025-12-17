---
layout: default
title: SportsGPT: An LLM-driven Framework for Interpretable Sports Motion Assessment and Training Guidance
---

# SportsGPT: An LLM-driven Framework for Interpretable Sports Motion Assessment and Training Guidance

**arXiv**: [2512.14121v1](https://arxiv.org/abs/2512.14121) | [PDF](https://arxiv.org/pdf/2512.14121.pdf)

**作者**: Wenbo Tian, Ruting Lin, Hongxian Zheng, Yaodong Yang, Geng Wu, Zihao Zhang, Zhang Zhang

**分类**: cs.CV, cs.AI

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**SportsGPT：一个基于LLM的可解释运动评估与训练指导框架**

🎯 **匹配领域**: **强化学习与模仿学习 (RL & IL)**

**关键词**: `运动分析` `大型语言模型` `运动评估` `训练指导` `时间序列对齐` `关键帧提取` `可解释性` `检索增强生成`

## 📋 核心要点

1. 现有运动分析系统缺乏自动性能诊断和可解释的训练指导，限制了其应用价值。
2. SportsGPT利用LLM，结合运动分析技术，构建从运动数据到专业训练指导的闭环系统。
3. 实验表明，SportsGPT在关键帧提取、诊断准确性和专业性方面均优于传统方法和通用LLM。

## 📝 摘要（中文）

现有的智能运动分析系统主要集中在“评分和可视化”上，缺乏自动性能诊断和可解释的训练指导。大型语言模型（LLM）和运动分析技术的最新进展为解决上述局限性提供了新的机会。本文提出了SportsGPT，一个基于LLM的可解释运动评估和训练指导框架，它建立了一个从运动时间序列输入到专业训练指导的闭环。首先，给定一组高质量的目标模型，我们引入了MotionDTW，一种为基于骨骼的运动序列精确关键帧提取而设计的两阶段时间序列对齐算法。随后，我们设计了一个基于知识的可解释运动评估模型（KISMAM），通过将关键帧与目标模型进行对比，获得一组可解释的评估指标（例如，伸展不足）。最后，我们提出了SportsRAG，一个基于Qwen3的RAG训练指导模型。利用一个6B token的知识库，它通过检索特定领域的问答对来提示LLM生成专业的训练指导。实验结果表明，MotionDTW显著优于传统方法，具有更低的时间误差和更高的IoU分数。此外，消融研究验证了KISMAM和SportsRAG，证实了SportsGPT在诊断准确性和专业性方面超越了通用LLM。

## 🔬 方法详解

**问题定义**：现有智能运动分析系统主要集中于评分和可视化，缺乏自动化的性能诊断和可解释的训练指导。这使得用户难以理解自身动作的不足之处，也无法获得个性化的训练建议。因此，如何从运动数据中提取有意义的评估指标，并生成专业的训练指导，是本文要解决的核心问题。

**核心思路**：SportsGPT的核心思路是利用大型语言模型（LLM）的强大推理和生成能力，结合运动分析技术，构建一个可解释的运动评估和训练指导框架。通过将运动数据转化为LLM可以理解的文本信息，并利用领域知识库进行增强，从而实现自动化的性能诊断和个性化的训练指导。

**技术框架**：SportsGPT框架包含三个主要模块：MotionDTW、KISMAM和SportsRAG。首先，MotionDTW用于从运动时间序列中提取关键帧。然后，KISMAM将提取的关键帧与目标模型进行对比，生成可解释的评估指标。最后，SportsRAG利用这些评估指标和领域知识库，生成专业的训练指导。整个框架形成一个闭环，从运动数据输入到训练指导输出。

**关键创新**：SportsGPT的关键创新在于将LLM应用于运动分析领域，并构建了一个可解释的运动评估和训练指导框架。与传统的运动分析系统相比，SportsGPT能够提供更深入的性能诊断和更个性化的训练指导。此外，MotionDTW算法和KISMAM模型也是重要的技术创新，它们分别提高了关键帧提取的准确性和评估指标的可解释性。

**关键设计**：MotionDTW采用两阶段时间序列对齐算法，旨在提高关键帧提取的准确性。KISMAM模型通过对比关键帧与目标模型，生成一组可解释的评估指标，例如伸展不足、角度偏差等。SportsRAG模型基于Qwen3，并利用一个6B token的知识库，通过检索特定领域的问答对来提示LLM生成专业的训练指导。具体参数设置和损失函数等细节在论文正文中应该有更详细的描述（未知）。

## 📊 实验亮点

实验结果表明，MotionDTW在关键帧提取方面显著优于传统方法，具有更低的时间误差和更高的IoU分数。消融研究验证了KISMAM和SportsRAG的有效性，证实了SportsGPT在诊断准确性和专业性方面超越了通用LLM。这些结果表明，SportsGPT在运动评估和训练指导方面具有显著的优势。

## 🎯 应用场景

SportsGPT具有广泛的应用前景，可应用于专业运动员训练、大众健身指导、康复训练等领域。通过提供个性化的运动评估和训练指导，SportsGPT可以帮助用户提高运动技能、预防运动损伤、改善身体健康。未来，SportsGPT还可以与其他智能设备（如智能穿戴设备）集成，实现更便捷的运动监测和指导。

## 📄 摘要（原文）

> Existing intelligent sports analysis systems mainly focus on "scoring and visualization," often lacking automatic performance diagnosis and interpretable training guidance. Recent advances of Large Language Models (LMMs) and motion analysis techniques provide new opportunities to address the above limitations. In this paper, we propose SportsGPT, an LLM-driven framework for interpretable sports motion assessment and training guidance, which establishes a closed loop from motion time-series input to professional training guidance. First, given a set of high-quality target models, we introduce MotionDTW, a two-stage time series alignment algorithm designed for accurate keyframe extraction from skeleton-based motion sequences. Subsequently, we design a Knowledge-based Interpretable Sports Motion Assessment Model (KISMAM) to obtain a set of interpretable assessment metrics (e.g., insufficient extension) by constrasting the keyframes with the targe models. Finally, we propose SportsRAG, a RAG-based training guidance model based on Qwen3. Leveraging a 6B-token knowledge base, it prompts the LLM to generate professional training guidance by retrieving domain-specific QA pairs. Experimental results demonstrate that MotionDTW significantly outperforms traditional methods with lower temporal error and higher IoU scores. Furthermore, ablation studies validate the KISMAM and SportsRAG, confirming that SportsGPT surpasses general LLMs in diagnostic accuracy and professionalism.

