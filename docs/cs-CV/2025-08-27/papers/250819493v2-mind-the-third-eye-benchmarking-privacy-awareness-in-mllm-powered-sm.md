---
layout: default
title: "Mind the Third Eye! Benchmarking Privacy Awareness in MLLM-powered Smartphone Agents"
---

# Mind the Third Eye! Benchmarking Privacy Awareness in MLLM-powered Smartphone Agents

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.19493" class="toolbar-btn" target="_blank">📄 arXiv: 2508.19493v2</a>
  <a href="https://arxiv.org/pdf/2508.19493.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.19493v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.19493v2', 'Mind the Third Eye! Benchmarking Privacy Awareness in MLLM-powered Smartphone Agents')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Zhixin Lin, Jungang Li, Shidong Pan, Yibo Shi, Yue Yao, Dongliang Xu

**分类**: cs.CR, cs.CV

**发布日期**: 2025-08-27 (更新: 2025-09-03)

**🔗 代码/项目**: [PROJECT_PAGE](https://zhixin-l.github.io/SAPA-Bench)

---

## 💡 一句话要点

**提出大规模基准以评估智能手机代理的隐私意识**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `隐私意识` `多模态语言模型` `智能手机代理` `基准测试` `用户隐私` `敏感信息`

## 📋 核心要点

1. 现有的智能手机代理在隐私意识方面表现不佳，尤其是在处理敏感信息时，许多代理未能有效识别和保护用户隐私。
2. 本文提出了一个大规模的基准测试，涵盖7138种场景，并对隐私上下文进行了详细注释，以评估智能手机代理的隐私意识。
3. 实验结果显示，闭源代理在隐私能力上优于开源代理，且隐私检测能力与场景的敏感性水平密切相关。

## 📝 摘要（中文）

智能手机为用户带来了极大的便利，但也使设备能够广泛记录各种个人信息。现有的多模态大型语言模型（MLLM）驱动的智能手机代理在自动化任务方面表现出色，但在操作过程中却获得了对用户敏感信息的广泛访问。为深入了解这些代理的隐私意识，本文首次提出了一个涵盖7138种场景的大规模基准，并对隐私上下文进行了类型、敏感性和位置的注释。结果表明，几乎所有被评估的代理在隐私意识方面表现不佳，得分均低于60%。总体而言，闭源代理的隐私能力优于开源代理，Gemini 2.0-flash表现最佳，隐私意识得分为67%。

## 🔬 方法详解

**问题定义**：本文旨在解决智能手机代理在处理用户敏感信息时隐私意识不足的问题。现有方法未能有效评估代理对隐私的保护能力，导致用户信息面临风险。

**核心思路**：通过构建一个涵盖7138种场景的大规模基准，论文提供了一个系统化的评估框架，以量化智能手机代理的隐私意识。该基准通过对隐私上下文进行详细注释，帮助研究者理解代理在不同场景下的表现。

**技术框架**：整体架构包括数据收集、场景注释、代理评估和结果分析四个主要模块。首先收集多种场景数据，然后对每个场景进行隐私类型和敏感性标注，最后对七个主流智能手机代理进行评估。

**关键创新**：本研究的创新点在于首次提出了一个系统化的隐私意识评估基准，涵盖了多种场景和隐私上下文，填补了现有研究的空白。与以往的研究相比，本文提供了更全面的评估方法。

**关键设计**：在实验中，采用了多种隐私类型和敏感性等级的场景进行评估，设计了相应的评分标准，以确保评估结果的客观性和准确性。

## 📊 实验亮点

实验结果显示，所有被评估的智能手机代理在隐私意识方面的表现均低于60%，其中闭源代理的表现优于开源代理。Gemini 2.0-flash的隐私意识得分为67%，是所有代理中表现最佳的。研究还发现，代理的隐私检测能力与场景的敏感性水平密切相关。

## 🎯 应用场景

该研究的潜在应用领域包括智能手机助手、个人信息管理和隐私保护技术。通过提高智能手机代理的隐私意识，可以增强用户对设备的信任，促进更安全的个人信息处理。未来，研究结果可能推动隐私保护技术的发展，促使开发者在设计智能代理时更加重视用户隐私。

## 📄 摘要（原文）

> Smartphones bring significant convenience to users but also enable devices to extensively record various types of personal information. Existing smartphone agents powered by Multimodal Large Language Models (MLLMs) have achieved remarkable performance in automating different tasks. However, as the cost, these agents are granted substantial access to sensitive users' personal information during this operation. To gain a thorough understanding of the privacy awareness of these agents, we present the first large-scale benchmark encompassing 7,138 scenarios to the best of our knowledge. In addition, for privacy context in scenarios, we annotate its type (e.g., Account Credentials), sensitivity level, and location. We then carefully benchmark seven available mainstream smartphone agents. Our results demonstrate that almost all benchmarked agents show unsatisfying privacy awareness (RA), with performance remaining below 60% even with explicit hints. Overall, closed-source agents show better privacy ability than open-source ones, and Gemini 2.0-flash achieves the best, achieving an RA of 67%. We also find that the agents' privacy detection capability is highly related to scenario sensitivity level, i.e., the scenario with a higher sensitivity level is typically more identifiable. We hope the findings enlighten the research community to rethink the unbalanced utility-privacy tradeoff about smartphone agents. Our code and benchmark are available at https://zhixin-l.github.io/SAPA-Bench.

