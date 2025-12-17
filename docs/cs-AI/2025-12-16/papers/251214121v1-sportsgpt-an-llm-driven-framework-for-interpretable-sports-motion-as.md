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

**提出SportsGPT框架，基于LLM实现可解释的运动评估与训练指导，解决现有系统缺乏自动诊断和可解释指导的问题。**

**关键词**: `运动分析` `大型语言模型` `时间序列对齐` `可解释评估` `检索增强生成` `骨架运动` `训练指导` `闭环框架`

## 📋 核心要点

1. 现有智能运动分析系统主要聚焦于评分和可视化，缺乏自动性能诊断和可解释的训练指导，限制了实际应用价值。
2. 论文提出SportsGPT框架，结合MotionDTW关键帧提取、KISMAM评估模型和SportsRAG指导生成，实现从运动输入到专业指导的闭环。
3. 实验显示MotionDTW在时间对齐上优于传统方法，SportsGPT在诊断准确性和专业性上超越通用LLMs，验证了框架有效性。

## 📝 摘要（中文）

现有的智能运动分析系统主要关注“评分和可视化”，往往缺乏自动性能诊断和可解释的训练指导。大型语言模型（LLMs）和运动分析技术的最新进展为解决上述局限性提供了新机遇。本文提出SportsGPT，一个基于LLM的可解释运动评估与训练指导框架，建立了从运动时间序列输入到专业训练指导的闭环。首先，给定一组高质量目标模型，我们引入MotionDTW，一种两阶段时间序列对齐算法，用于从基于骨架的运动序列中准确提取关键帧。随后，我们设计了一个基于知识的可解释运动评估模型（KISMAM），通过将关键帧与目标模型对比，获得一组可解释的评估指标（如伸展不足）。最后，我们提出SportsRAG，一个基于Qwen3的RAG训练指导模型。利用一个6B-token的知识库，它通过检索领域特定的问答对来提示LLM生成专业训练指导。实验结果表明，MotionDTW在时间误差更低和IoU分数更高方面显著优于传统方法。此外，消融研究验证了KISMAM和SportsRAG，确认SportsGPT在诊断准确性和专业性方面超越通用LLMs。

## 🔬 方法详解

SportsGPT是一个基于LLM的闭环框架，从运动时间序列输入到专业训练指导。核心方法包括：MotionDTW，一种两阶段时间序列对齐算法，用于从骨架序列中准确提取关键帧；KISMAM，基于知识的可解释运动评估模型，通过对比关键帧与目标模型生成可解释指标；SportsRAG，基于RAG的训练指导模型，利用6B-token知识库和Qwen3 LLM，通过检索领域QA对生成专业指导。关键创新在于将运动分析与LLM结合，实现可解释评估和个性化指导。与现有方法的主要区别在于，它不仅提供评分，还通过知识驱动和RAG机制，生成具体、可解释的诊断和改进建议，解决了传统系统缺乏深度分析和指导的问题。

## 📊 实验亮点

MotionDTW在关键帧提取上显著优于传统方法，时间误差更低，IoU分数更高；SportsGPT通过消融研究验证，在诊断准确性和专业性方面超越通用LLMs，展示了框架的整体优势。

## 🎯 应用场景

该研究可应用于体育训练、康复医学和健身指导等领域，为运动员、教练和普通用户提供自动、可解释的运动性能评估和个性化训练建议，提升训练效率和安全性。

## 📄 摘要（原文）

> Existing intelligent sports analysis systems mainly focus on "scoring and visualization," often lacking automatic performance diagnosis and interpretable training guidance. Recent advances of Large Language Models (LMMs) and motion analysis techniques provide new opportunities to address the above limitations. In this paper, we propose SportsGPT, an LLM-driven framework for interpretable sports motion assessment and training guidance, which establishes a closed loop from motion time-series input to professional training guidance. First, given a set of high-quality target models, we introduce MotionDTW, a two-stage time series alignment algorithm designed for accurate keyframe extraction from skeleton-based motion sequences. Subsequently, we design a Knowledge-based Interpretable Sports Motion Assessment Model (KISMAM) to obtain a set of interpretable assessment metrics (e.g., insufficient extension) by constrasting the keyframes with the targe models. Finally, we propose SportsRAG, a RAG-based training guidance model based on Qwen3. Leveraging a 6B-token knowledge base, it prompts the LLM to generate professional training guidance by retrieving domain-specific QA pairs. Experimental results demonstrate that MotionDTW significantly outperforms traditional methods with lower temporal error and higher IoU scores. Furthermore, ablation studies validate the KISMAM and SportsRAG, confirming that SportsGPT surpasses general LLMs in diagnostic accuracy and professionalism.

