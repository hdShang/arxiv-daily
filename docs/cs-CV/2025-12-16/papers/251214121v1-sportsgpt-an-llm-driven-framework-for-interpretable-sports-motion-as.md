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

**提出SportsGPT框架，通过运动序列对齐与知识增强，实现可解释的运动评估与训练指导。**

🎯 **匹配领域**: **强化学习**

**关键词**: `运动分析` `时间序列对齐` `可解释评估` `检索增强生成` `大型语言模型` `骨架动作识别` `智能训练指导` `闭环系统`

## 📋 核心要点

1. 现有智能体育分析系统多聚焦于评分与可视化，缺乏自动诊断与可解释指导，限制了实际训练应用。
2. 提出SportsGPT框架，结合MotionDTW对齐算法、KISMAM评估模型和SportsRAG指导模型，实现闭环运动分析。
3. 实验显示MotionDTW降低时间误差、提升IoU，SportsGPT在诊断准确性和专业性上优于通用LLM。

## 📝 摘要（中文）

现有的智能体育分析系统主要关注“评分与可视化”，往往缺乏自动性能诊断和可解释的训练指导。大型语言模型和运动分析技术的最新进展为解决上述局限提供了新机遇。本文提出SportsGPT，一个基于LLM的可解释运动评估与训练指导框架，建立了从运动时间序列输入到专业训练指导的闭环。首先，给定一组高质量目标模型，我们引入MotionDTW，一种两阶段时间序列对齐算法，用于从基于骨架的运动序列中准确提取关键帧。随后，我们设计了一个基于知识的可解释运动评估模型，通过对比关键帧与目标模型，获得一组可解释的评估指标。最后，我们提出SportsRAG，一个基于Qwen3的RAG训练指导模型，利用6B-token的知识库，通过检索领域特定的问答对，提示LLM生成专业训练指导。实验结果表明，MotionDTW在时间误差和IoU分数上显著优于传统方法。此外，消融研究验证了KISMAM和SportsRAG，确认SportsGPT在诊断准确性和专业性方面超越通用LLM。

## 🔬 方法详解

**问题定义**：论文旨在解决智能体育分析中缺乏自动性能诊断和可解释训练指导的问题。现有方法多停留在运动数据的评分与可视化层面，无法提供深入的错误分析和个性化改进建议，限制了其在专业训练中的应用价值。

**核心思路**：论文的核心思路是构建一个从运动时间序列输入到专业训练指导的闭环框架。通过精确对齐运动序列、提取可解释评估指标，并利用大型语言模型生成指导，实现端到端的智能分析。这种设计结合了传统运动分析与现代AI技术，以提升系统的实用性和专业性。

**技术框架**：整体架构包含三个主要阶段：首先，使用MotionDTW算法对输入的运动序列进行两阶段时间序列对齐，提取关键帧；其次，通过KISMAM模型对比关键帧与目标模型，生成可解释的评估指标；最后，基于SportsRAG模型，利用检索增强生成技术，从知识库中检索相关信息，驱动LLM生成专业训练指导。

**关键创新**：最重要的技术创新包括MotionDTW算法，它通过两阶段对齐提高了关键帧提取的准确性；KISMAM模型，它引入了基于知识的评估机制，增强了结果的可解释性；以及SportsRAG模型，它结合RAG技术与大型语言模型，提升了指导的专业性和针对性。这些创新使系统超越了传统的评分系统，实现了更深入的交互式分析。

**关键设计**：在技术细节上，MotionDTW采用两阶段动态时间规整算法，具体参数未详细说明，但强调其优化了时间误差和IoU分数；KISMAM基于对比学习框架，利用目标模型作为参考，生成如“伸展不足”等具体指标；SportsRAG基于Qwen3 LLM，构建了包含6B-token的领域知识库，通过检索QA对来增强提示，具体网络结构和损失函数在论文中未明确描述，但突出了其RAG机制的有效性。

## 📊 实验亮点

实验结果显示，MotionDTW在关键帧提取上显著优于传统方法，具体表现为更低的时间误差和更高的IoU分数，但论文未提供具体数值。消融研究验证了KISMAM和SportsRAG的有效性，SportsGPT在诊断准确性和专业性方面超越通用LLM，例如在生成训练指导时更符合领域知识，但未给出量化提升幅度。

## 🎯 应用场景

该研究在体育训练、康复医学和健身指导等领域具有广泛应用潜力。例如，可用于专业运动员的动作优化、普通用户的健身错误纠正，或物理治疗中的运动功能评估。其价值在于提供自动、可解释的反馈，降低教练依赖，提升训练效率。未来可能推动智能体育设备的集成，促进个性化健康管理的发展。

## 📄 摘要（原文）

> Existing intelligent sports analysis systems mainly focus on "scoring and visualization," often lacking automatic performance diagnosis and interpretable training guidance. Recent advances of Large Language Models (LMMs) and motion analysis techniques provide new opportunities to address the above limitations. In this paper, we propose SportsGPT, an LLM-driven framework for interpretable sports motion assessment and training guidance, which establishes a closed loop from motion time-series input to professional training guidance. First, given a set of high-quality target models, we introduce MotionDTW, a two-stage time series alignment algorithm designed for accurate keyframe extraction from skeleton-based motion sequences. Subsequently, we design a Knowledge-based Interpretable Sports Motion Assessment Model (KISMAM) to obtain a set of interpretable assessment metrics (e.g., insufficient extension) by constrasting the keyframes with the targe models. Finally, we propose SportsRAG, a RAG-based training guidance model based on Qwen3. Leveraging a 6B-token knowledge base, it prompts the LLM to generate professional training guidance by retrieving domain-specific QA pairs. Experimental results demonstrate that MotionDTW significantly outperforms traditional methods with lower temporal error and higher IoU scores. Furthermore, ablation studies validate the KISMAM and SportsRAG, confirming that SportsGPT surpasses general LLMs in diagnostic accuracy and professionalism.

