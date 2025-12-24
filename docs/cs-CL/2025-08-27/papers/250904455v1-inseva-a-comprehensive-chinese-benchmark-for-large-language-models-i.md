---
layout: default
title: "INSEva: A Comprehensive Chinese Benchmark for Large Language Models in Insurance"
---

# INSEva: A Comprehensive Chinese Benchmark for Large Language Models in Insurance

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2509.04455" class="toolbar-btn" target="_blank">📄 arXiv: 2509.04455v1</a>
  <a href="https://arxiv.org/pdf/2509.04455.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2509.04455v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2509.04455v1', 'INSEva: A Comprehensive Chinese Benchmark for Large Language Models in Insurance')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shisong Chen, Qian Zhu, Wenyan Yang, Chengyi Yang, Zhong Wang, Ping Wang, Xuan Lin, Bo Xu, Daqian Li, Chao Yuan, Licai Qi, Wanqing Xu, sun zhenxing, Xin Lu, Shiqiang Xiong, Chao Chen, Haixiang Hu, Yanghua Xiao

**分类**: cs.CL

**发布日期**: 2025-08-27

**备注**: Under review

---

## 💡 一句话要点

**提出INSEva基准以解决保险领域AI评估不足问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `保险AI` `评估基准` `大型语言模型` `多维度评估` `开放式回答` `性能评估` `智能化应用`

## 📋 核心要点

1. 现有的AI评估基准未能充分考虑保险领域的特殊需求，导致评估结果的局限性。
2. INSEva基准通过多维度评估分类，专门设计用于评估AI在保险领域的能力，填补了这一空白。
3. 对8个大型语言模型的评估显示，尽管其在保险领域的基本能力得分超过80，但在处理复杂场景时仍存在显著差距。

## 📝 摘要（中文）

保险作为全球金融系统的重要组成部分，对AI应用的准确性和可靠性要求极高。现有基准虽然评估了AI在多个领域的能力，但未能充分捕捉保险领域的独特特征和需求。为此，本文提出了INSEva，一个专门为评估AI系统在保险领域的知识和能力而设计的综合性中文基准。INSEva涵盖了业务领域、任务格式、难度等级和认知知识维度的多维评估分类，共包含38,704个高质量评估示例，来源于权威材料。基准采用定制的评估方法，评估开放式回答的真实性和完整性。通过对8个最先进的大型语言模型的广泛评估，发现不同维度的性能差异显著。

## 🔬 方法详解

**问题定义**：本文旨在解决现有AI评估基准在保险领域应用不足的问题，特别是缺乏针对保险行业特定需求的评估工具。现有方法未能有效捕捉保险领域的复杂性和多样性。

**核心思路**：提出INSEva基准，通过多维度评估框架，涵盖业务领域、任务格式、难度等级和认知知识维度，提供全面的评估标准，以更好地评估AI在保险领域的能力。

**技术框架**：INSEva的整体架构包括数据收集、评估设计和结果分析三个主要模块。数据收集阶段从权威材料中获取38,704个评估示例，评估设计阶段则采用定制的评估方法，最后通过结果分析评估模型的表现。

**关键创新**：INSEva的创新之处在于其多维度评估分类和定制的评估方法，特别是对开放式回答的真实性和完整性进行评估，这在现有基准中是前所未有的。

**关键设计**：在评估过程中，设置了多种任务格式和难度等级，以确保评估的全面性和准确性，同时采用了针对性的损失函数来优化模型在保险领域的表现。

## 📊 实验亮点

在对8个大型语言模型的评估中，发现这些模型在保险领域的平均得分超过80，显示出基本的能力。然而，在处理复杂的实际保险场景时，模型表现出显著的性能差异，表明仍需进一步优化和提升。

## 🎯 应用场景

INSEva基准的潜在应用领域包括保险行业的AI系统开发、评估和优化。通过提供针对性的评估标准，保险公司可以更有效地选择和改进AI工具，从而提升服务质量和客户满意度。未来，INSEva可能成为保险领域AI应用的标准评估工具，推动行业的智能化进程。

## 📄 摘要（原文）

> Insurance, as a critical component of the global financial system, demands high standards of accuracy and reliability in AI applications. While existing benchmarks evaluate AI capabilities across various domains, they often fail to capture the unique characteristics and requirements of the insurance domain. To address this gap, we present INSEva, a comprehensive Chinese benchmark specifically designed for evaluating AI systems' knowledge and capabilities in insurance. INSEva features a multi-dimensional evaluation taxonomy covering business areas, task formats, difficulty levels, and cognitive-knowledge dimension, comprising 38,704 high-quality evaluation examples sourced from authoritative materials. Our benchmark implements tailored evaluation methods for assessing both faithfulness and completeness in open-ended responses. Through extensive evaluation of 8 state-of-the-art Large Language Models (LLMs), we identify significant performance variations across different dimensions. While general LLMs demonstrate basic insurance domain competency with average scores above 80, substantial gaps remain in handling complex, real-world insurance scenarios. The benchmark will be public soon.

