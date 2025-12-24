---
layout: default
title: "Drifting Away from Truth: GenAI-Driven News Diversity Challenges LVLM-Based Misinformation Detection"
---

# Drifting Away from Truth: GenAI-Driven News Diversity Challenges LVLM-Based Misinformation Detection

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.12711" class="toolbar-btn" target="_blank">📄 arXiv: 2508.12711v4</a>
  <a href="https://arxiv.org/pdf/2508.12711.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.12711v4" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.12711v4', 'Drifting Away from Truth: GenAI-Driven News Diversity Challenges LVLM-Based Misinformation Detection')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Fanxiao Li, Jiaying Wu, Tingchao Fu, Yunyun Dong, Bingbing Song, Wei Zhou

**分类**: cs.CV

**发布日期**: 2025-08-18 (更新: 2025-12-23)

---

## 💡 一句话要点

**提出DriftBench以解决GenAI驱动的新闻多样性对虚假信息检测的挑战**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `多模态虚假信息检测` `生成性人工智能` `新闻多样性` `鲁棒性评估` `模型脆弱性`

## 📋 核心要点

1. 现有的多模态虚假信息检测方法在面对GenAI驱动的新闻多样性时表现出显著的脆弱性，导致误判和证据质量下降。
2. 论文提出了DriftBench基准，旨在系统性地评估和分析多层次漂移对虚假信息检测的影响。
3. 实验结果表明，六个最先进的LVLM基础检测器在多层次漂移下平均F1分数下降了14.8%，推理一致性显著降低。

## 📝 摘要（中文）

多模态虚假信息的泛滥对公共话语和社会信任构成了日益严重的威胁。尽管大型视觉语言模型（LVLMs）在多模态虚假信息检测（MMD）方面取得了进展，但生成性人工智能（GenAI）工具的兴起带来了新的挑战：GenAI驱动的新闻多样性。这种多样性引发了多层次的漂移，包括模型层面的误判漂移和证据层面的漂移，显著降低了现有LVLM基础的MMD系统的鲁棒性。为系统研究这一问题，本文引入了一个大规模基准DriftBench，包含16,000个新闻实例，设计了三项评估任务。实验结果显示，现有检测器在多层次漂移下性能显著下降，推理轨迹不稳定，尤其在对抗性证据注入下表现更为严重。

## 🔬 方法详解

**问题定义**：本文旨在解决GenAI驱动的新闻多样性对现有多模态虚假信息检测系统的影响，现有方法在面对多样化内容时表现出鲁棒性不足和误判率高的问题。

**核心思路**：通过引入DriftBench基准，系统性地评估多层次漂移对虚假信息检测的影响，分析模型在不同层次漂移下的表现和脆弱性。

**技术框架**：整体架构包括数据收集、漂移分类、评估任务设计和实验分析四个主要模块。数据收集阶段涵盖16,000个新闻实例，漂移分类则分为模型层面和证据层面。

**关键创新**：引入了多层次漂移的概念，揭示了现有LVLM基础MMD系统的基本脆弱性，强调了在GenAI时代需要更具鲁棒性的检测方法。

**关键设计**：设计了三项评估任务，分别针对真相验证的鲁棒性、对抗性证据的易受攻击性和推理一致性分析，采用了多种性能指标进行综合评估。实验中使用了六个最先进的LVLM基础检测器进行对比。

## 📊 实验亮点

实验结果显示，在多层次漂移的影响下，六个最先进的LVLM基础检测器的平均F1分数下降了14.8%，推理轨迹变得不稳定，尤其在对抗性证据注入的情况下，表现出更为严重的性能下降。

## 🎯 应用场景

该研究的潜在应用领域包括新闻媒体、社交网络和信息验证平台，能够帮助提升虚假信息检测系统的鲁棒性，增强公众对信息的信任。未来，随着GenAI技术的进一步发展，研究成果将对信息传播和社会信任的维护产生深远影响。

## 📄 摘要（原文）

> The proliferation of multimodal misinformation poses growing threats to public discourse and societal trust. While Large Vision-Language Models (LVLMs) have enabled recent progress in multimodal misinformation detection (MMD), the rise of generative AI (GenAI) tools introduces a new challenge: GenAI-driven news diversity, characterized by highly varied and complex content. We show that this diversity induces multi-level drift, comprising (1) model-level misperception drift, where stylistic variations disrupt a model's internal reasoning, and (2) evidence-level drift, where expression diversity degrades the quality or relevance of retrieved external evidence. These drifts significantly degrade the robustness of current LVLM-based MMD systems. To systematically study this problem, we introduce DriftBench, a large-scale benchmark comprising 16,000 news instances across six categories of diversification. We design three evaluation tasks: (1) robustness of truth verification under multi-level drift; (2) susceptibility to adversarial evidence contamination generated by GenAI; and (3) analysis of reasoning consistency across diverse inputs. Experiments with six state-of-the-art LVLM-based detectors show substantial performance drops (average F1 -14.8%) and increasingly unstable reasoning traces, with even more severe failures under adversarial evidence injection. Our findings uncover fundamental vulnerabilities in existing MMD systems and suggest an urgent need for more resilient approaches in the GenAI era.

