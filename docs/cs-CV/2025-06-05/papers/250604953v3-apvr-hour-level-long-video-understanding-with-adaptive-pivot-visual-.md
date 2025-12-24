---
layout: default
title: "APVR: Hour-Level Long Video Understanding with Adaptive Pivot Visual Information Retrieval"
---

# APVR: Hour-Level Long Video Understanding with Adaptive Pivot Visual Information Retrieval

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.04953" class="toolbar-btn" target="_blank">📄 arXiv: 2506.04953v3</a>
  <a href="https://arxiv.org/pdf/2506.04953.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.04953v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.04953v3', 'APVR: Hour-Level Long Video Understanding with Adaptive Pivot Visual Information Retrieval')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Hong Gao, Yiming Bao, Xuezhen Tu, Bin Zhong, Linan Yue, Minling Zhang

**分类**: cs.CV

**发布日期**: 2025-06-05 (更新: 2025-11-15)

**备注**: Accepted by AAAI 2026

---

## 💡 一句话要点

**提出APVR以解决长视频理解中的信息检索问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `自适应检索` `多模态学习` `视觉信息处理` `无训练方法`

## 📋 核心要点

1. 现有多模态大型语言模型在处理小时级视频时面临内存和资源限制，导致理解能力不足。
2. 本文提出的APVR框架通过分层检索重要视觉信息，采用枢轴帧和枢轴令牌检索技术，解决了信息不足的问题。
3. 实验结果显示，APVR在LongVideoBench、VideoMME和MLVU基准上分别提升了9.5%、4.6%和9.7%的性能，达到最先进水平。

## 📝 摘要（中文）

当前的多模态大型语言模型在小时级视频理解方面面临重大挑战，不仅需要处理大量信息，还需克服训练和推理中的内存限制。尽管近期的无训练方法通过压缩视觉特征减轻了资源需求，但对不完整视觉信息的依赖限制了性能潜力。为此，本文提出了自适应枢轴视觉信息检索（APVR），这是一个无训练框架，能够分层检索和保留足够且重要的视觉信息。APVR通过两个互补组件突破了内存限制：枢轴帧检索和枢轴令牌检索。实验结果表明，APVR在多个基准上显著提升了性能，达到了当前最先进的水平。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态大型语言模型在小时级视频理解中的内存和信息处理不足的问题。现有方法在处理长视频时，常常面临信息量大和资源消耗高的挑战。

**核心思路**：APVR框架通过自适应地检索和保留重要的视觉信息，采用分层检索策略来克服内存限制。通过枢轴帧检索和枢轴令牌检索，确保在处理长视频时保持语义的完整性。

**技术框架**：APVR的整体架构包括两个主要模块：枢轴帧检索模块和枢轴令牌检索模块。前者通过查询扩展和迭代的时空语义置信度评分来识别相关视频帧，后者则在最多1024个枢轴帧内进行基于查询的注意力驱动的令牌选择。

**关键创新**：APVR的创新之处在于其双粒度检索策略，能够有效地从长视频中提取重要信息，突破了传统方法在内存和信息完整性上的局限。

**关键设计**：在设计上，APVR采用了查询扩展和时空语义置信度评分等技术细节，以确保检索的准确性和有效性，同时保持较低的资源消耗。

## 📊 实验亮点

APVR在LongVideoBench、VideoMME和MLVU基准上分别实现了9.5%、4.6%和9.7%的性能提升，显著优于现有的训练和无训练方法，展示了其在长视频理解中的有效性和先进性。

## 🎯 应用场景

APVR的研究成果在视频分析、内容检索和智能监控等领域具有广泛的应用潜力。通过提高长视频理解的效率和准确性，该框架可以为多媒体信息处理和智能决策提供更强大的支持，推动相关技术的发展和应用。

## 📄 摘要（原文）

> Current multimodal large language models (MLLMs) struggle with hour-level video understanding, facing significant challenges not only in modeling the substantial information volume of long videos but also in overcoming the memory wall and resource constraints during both training and inference. Although recent training-free approaches have alleviated resource demands by compressing visual features, their reliance on incomplete visual information limits the performance potential. To address these limitations, we propose Adaptive Pivot Visual information Retrieval (APVR), a training-free framework that hierarchically retrieves and retains sufficient and important visual information. It breakthroughs the memory wall limitation via two complementary components: Pivot Frame Retrieval employs query expansion and iterative spatio-semantic confidence scoring to identify relevant video frames, and Pivot Token Retrieval performs query-aware attention-driven token selection within up to 1024 pivot frames. This dual granularity approach enables the processing of hour-long videos while maintaining semantic fidelity. Experimental validations on three different baseline MLLMs demonstrate significant performance improvements up to 9.5\%, 4.6\% and 9.7\% on LongVideoBench, VideoMME and MLVU, respectively. APVR achieves state-of-the-art results for both training-free and training-based approaches.

