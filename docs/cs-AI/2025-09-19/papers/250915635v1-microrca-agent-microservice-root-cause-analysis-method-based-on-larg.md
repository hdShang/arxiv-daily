---
layout: default
title: "MicroRCA-Agent: Microservice Root Cause Analysis Method Based on Large Language Model Agents"
---

# MicroRCA-Agent: Microservice Root Cause Analysis Method Based on Large Language Model Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.15635" class="toolbar-btn" target="_blank">📄 arXiv: 2509.15635v1</a>
  <a href="https://arxiv.org/pdf/2509.15635.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.15635v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.15635v1', 'MicroRCA-Agent: Microservice Root Cause Analysis Method Based on Large Language Model Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Pan Tang, Shixiang Tang, Huanqi Pu, Zhiqing Miao, Zhixing Wang

**分类**: cs.AI

**发布日期**: 2025-09-19

**备注**: 18 pages, 22 figures

**🔗 代码/项目**: [GITHUB](https://github.com/tangpan360/MicroRCA-Agent)

---

## 💡 一句话要点

**提出MicroRCA-Agent，利用大语言模型Agent进行微服务根因分析**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `微服务` `根因分析` `大语言模型` `多模态融合` `异常检测`

## 📋 核心要点

1. 现有微服务根因分析方法难以有效融合多模态数据，导致定位精度不足，且缺乏对全栈现象的有效总结。
2. MicroRCA-Agent通过结合日志解析、双重异常检测和统计过滤，并利用大语言模型的跨模态理解能力，实现精准根因定位。
3. 实验结果表明，MicroRCA-Agent在复杂微服务故障场景中表现出色，最终得分达到50.71，验证了其有效性。

## 📝 摘要（中文）

本文提出了一种基于大语言模型Agent的微服务根因分析创新解决方案MicroRCA-Agent，它构建了一个具有多模态数据融合的智能故障根因定位系统。技术创新体现在三个关键方面：首先，结合预训练的Drain日志解析算法和多级数据过滤机制，高效地将海量日志压缩为高质量的故障特征。其次，采用双重异常检测方法，将Isolation Forest无监督学习算法与状态码验证相结合，实现全面的链路异常识别。第三，设计了一种统计对称比率过滤机制，结合两阶段LLM分析策略，以实现跨节点-服务-Pod层次的全栈现象总结。多模态根因分析模块利用精心设计的跨模态提示，深入整合多模态异常信息，充分利用大语言模型的跨模态理解和逻辑推理能力，生成包含故障组件、根因描述和推理过程的结构化分析结果。全面的消融研究验证了每种模态数据的互补价值和系统架构的有效性。所提出的解决方案在复杂的微服务故障场景中表现出卓越的性能，最终得分为50.71。代码已在https://github.com/tangpan360/MicroRCA-Agent发布。

## 🔬 方法详解

**问题定义**：微服务架构的复杂性使得故障根因分析变得困难。现有方法难以有效融合日志、链路追踪等多种模态的数据，并且缺乏对全栈现象的有效总结，导致根因定位精度不高，耗时较长。因此，需要一种能够有效利用多模态数据，并具备全栈分析能力的根因分析方法。

**核心思路**：MicroRCA-Agent的核心思路是利用大语言模型（LLM）的强大理解和推理能力，将多模态的异常信息进行整合分析，从而实现精准的根因定位。通过预处理和过滤，将海量数据压缩为高质量的故障特征，然后利用LLM进行跨模态推理，最终生成结构化的分析结果。

**技术框架**：MicroRCA-Agent的整体架构包含以下几个主要模块：1) **日志特征提取**：利用预训练的Drain算法进行日志解析，并结合多级数据过滤机制，提取高质量的日志特征。2) **链路异常检测**：采用双重异常检测方法，结合Isolation Forest和状态码验证，识别链路中的异常。3) **全栈现象总结**：设计统计对称比率过滤机制，结合两阶段LLM分析策略，总结跨节点-服务-Pod层次的全栈现象。4) **多模态根因分析**：利用精心设计的跨模态提示，将多模态异常信息输入LLM，生成结构化的根因分析结果。

**关键创新**：MicroRCA-Agent的关键创新在于：1) **多模态数据融合**：通过LLM的跨模态理解能力，将日志、链路追踪等多种模态的数据进行有效融合。2) **全栈现象总结**：利用统计对称比率过滤机制和两阶段LLM分析策略，实现跨层次的全栈现象总结。3) **基于LLM的根因分析**：利用LLM的推理能力，生成结构化的根因分析结果，包括故障组件、根因描述和推理过程。

**关键设计**：在日志特征提取模块，采用了预训练的Drain算法，并结合多级数据过滤机制，以提高日志特征的质量。在链路异常检测模块，采用了Isolation Forest算法进行无监督学习，并结合状态码验证，以提高异常检测的准确率。在多模态根因分析模块，设计了精心设计的跨模态提示，以引导LLM进行有效的推理。

## 📊 实验亮点

实验结果表明，MicroRCA-Agent在复杂的微服务故障场景中表现出卓越的性能，最终得分为50.71。消融研究验证了每种模态数据的互补价值和系统架构的有效性，证明了多模态数据融合和LLM推理在根因分析中的重要作用。

## 🎯 应用场景

MicroRCA-Agent可应用于各种规模的微服务系统，帮助运维人员快速定位故障根因，缩短平均修复时间（MTTR），提高系统的可用性和稳定性。该研究成果对于提升云原生环境下的智能化运维水平具有重要意义，并可推广到其他复杂系统的故障诊断领域。

## 📄 摘要（原文）

> This paper presents MicroRCA-Agent, an innovative solution for microservice root cause analysis based on large language model agents, which constructs an intelligent fault root cause localization system with multimodal data fusion. The technical innovations are embodied in three key aspects: First, we combine the pre-trained Drain log parsing algorithm with multi-level data filtering mechanism to efficiently compress massive logs into high-quality fault features. Second, we employ a dual anomaly detection approach that integrates Isolation Forest unsupervised learning algorithms with status code validation to achieve comprehensive trace anomaly identification. Third, we design a statistical symmetry ratio filtering mechanism coupled with a two-stage LLM analysis strategy to enable full-stack phenomenon summarization across node-service-pod hierarchies. The multimodal root cause analysis module leverages carefully designed cross-modal prompts to deeply integrate multimodal anomaly information, fully exploiting the cross-modal understanding and logical reasoning capabilities of large language models to generate structured analysis results encompassing fault components, root cause descriptions, and reasoning trace. Comprehensive ablation studies validate the complementary value of each modal data and the effectiveness of the system architecture. The proposed solution demonstrates superior performance in complex microservice fault scenarios, achieving a final score of 50.71. The code has been released at: https://github.com/tangpan360/MicroRCA-Agent.

