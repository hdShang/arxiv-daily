---
layout: default
title: Threading Keyframe with Narratives: MLLMs as Strong Long Video Comprehenders
---

# Threading Keyframe with Narratives: MLLMs as Strong Long Video Comprehenders

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.24158" class="toolbar-btn" target="_blank">📄 arXiv: 2505.24158v1</a>
  <a href="https://arxiv.org/pdf/2505.24158.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.24158v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.24158v1', 'Threading Keyframe with Narratives: MLLMs as Strong Long Video Comprehenders')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Bo Fang, Wenhao Wu, Qiangqiang Wu, Yuxin Song, Antoni B. Chan

**分类**: cs.CV

**发布日期**: 2025-05-30

---

## 💡 一句话要点

**提出Nar-KFC模块以解决长视频理解中的关键帧选择问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `长视频理解` `多模态大语言模型` `关键帧选择` `文本叙述生成` `视频感知`

## 📋 核心要点

1. 现有方法在长视频理解中面临视频帧数量庞大与语言模型上下文长度有限的矛盾，导致信息选择不当。
2. 本文提出Nar-KFC模块，通过优化关键帧选择与插入文本叙述，提升长视频的感知能力。
3. 实验结果显示，Nar-KFC在多个长视频基准上显著提升了MLLM的性能，验证了其有效性。

## 📝 摘要（中文）

利用多模态大语言模型（MLLMs）进行长视频理解仍然面临挑战，主要是视频帧数量庞大与语言模型上下文长度有限之间的矛盾。传统的均匀采样方法常导致选择无关内容，而在数千帧上进行后训练则带来巨大的计算负担。本文提出了一种名为Nar-KFC的关键帧与叙述交织模块，旨在有效且高效地进行长视频感知。Nar-KFC包括两个协作步骤：首先，将关键帧选择过程形式化为整数二次规划问题，优化查询相关性和帧多样性；其次，通过插入从非关键帧生成的文本叙述，缓解稀疏关键帧采样造成的时间不连续性。实验结果表明，Nar-KFC显著提升了多种长视频基准上的MLLM性能。

## 🔬 方法详解

**问题定义**：本文旨在解决长视频理解中关键帧选择的效率与效果问题。现有方法往往因视频帧数量庞大而导致信息选择不当，影响理解效果。

**核心思路**：论文提出的Nar-KFC模块通过优化关键帧选择与插入文本叙述，形成连贯的时间序列表示，从而提升长视频的理解能力。

**技术框架**：Nar-KFC模块主要包括两个步骤：首先，使用整数二次规划优化关键帧的选择；其次，通过现成的图像描述生成器生成文本叙述，并将其插入关键帧之间，形成完整的时间序列。

**关键创新**：Nar-KFC的创新在于将关键帧选择与文本叙述生成相结合，形成了一种时间和内容感知的压缩策略，显著改善了传统方法的不足。

**关键设计**：在关键帧选择中，采用定制的贪婪搜索策略以降低计算复杂度；在文本叙述生成中，确保叙述与关键帧的时间顺序一致，以保持信息的连贯性。

## 📊 实验亮点

实验结果表明，Nar-KFC在多个长视频基准上显著提升了MLLM的性能，具体提升幅度达到XX%（具体数据待补充），相较于传统方法，表现出更强的理解能力和信息选择效率。

## 🎯 应用场景

该研究的潜在应用领域包括视频监控、自动视频摘要生成、智能视频检索等。通过提升长视频理解能力，Nar-KFC模块能够为多模态交互系统提供更准确的上下文理解，推动相关领域的发展与应用。

## 📄 摘要（原文）

> Employing Multimodal Large Language Models (MLLMs) for long video understanding remains a challenging problem due to the dilemma between the substantial number of video frames (i.e., visual tokens) versus the limited context length of language models. Traditional uniform sampling often leads to selection of irrelevant content, while post-training MLLMs on thousands of frames imposes a substantial computational burden. In this paper, we propose threading keyframes with narratives (Nar-KFC), a plug-and-play module to facilitate effective and efficient long video perception. Nar-KFC generally involves two collaborative steps. First, we formulate the keyframe selection process as an integer quadratic programming problem, jointly optimizing query-relevance and frame-diversity. To avoid its computational complexity, a customized greedy search strategy is designed as an efficient alternative. Second, to mitigate the temporal discontinuity caused by sparse keyframe sampling, we further introduce interleaved textual narratives generated from non-keyframes using off-the-shelf captioners. These narratives are inserted between keyframes based on their true temporal order, forming a coherent and compact representation. Nar-KFC thus serves as a temporal- and content-aware compression strategy that complements visual and textual modalities. Experimental results on multiple long-video benchmarks demonstrate that Nar-KFC significantly improves the performance of popular MLLMs. Code will be made publicly available.

