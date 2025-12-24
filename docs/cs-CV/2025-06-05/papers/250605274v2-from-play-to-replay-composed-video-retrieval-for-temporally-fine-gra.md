---
layout: default
title: "From Play to Replay: Composed Video Retrieval for Temporally Fine-Grained Videos"
---

# From Play to Replay: Composed Video Retrieval for Temporally Fine-Grained Videos

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.05274" class="toolbar-btn" target="_blank">📄 arXiv: 2506.05274v2</a>
  <a href="https://arxiv.org/pdf/2506.05274.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.05274v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.05274v2', 'From Play to Replay: Composed Video Retrieval for Temporally Fine-Grained Videos')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Animesh Gupta, Jay Parmar, Ishan Rajendrakumar Dave, Mubarak Shah

**分类**: cs.CV

**发布日期**: 2025-06-05 (更新: 2025-11-20)

---

## 💡 一句话要点

**提出TF-CoVR以解决细粒度视频检索问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `细粒度视频检索` `视频编码` `对比学习` `多模态检索` `体育视频分析`

## 📋 核心要点

1. 现有的CoVR方法主要关注外观变化，未能有效处理细粒度的时间差异，限制了其实际应用。
2. 本文提出TF-CoVR，构建了一个新的基准，利用大规模数据集和多目标视频关联，增强了检索的灵活性。
3. 实验结果表明，TF-CoVR-Base在零-shot和微调情况下均显著提升了检索性能，mAP@50从5.92提升至7.51，微调后达到27.22。

## 📝 摘要（中文）

Composed Video Retrieval (CoVR)旨在根据查询视频和描述修改的文本检索目标视频。现有的CoVR基准主要关注外观变化或粗略事件变化，未能有效捕捉细微、快速的时间差异。为此，本文引入TF-CoVR，这是首个专注于细粒度CoVR的大规模基准，涵盖体操和跳水领域，提供来自FineGym和FineDiving数据集的18万对三元组。TF-CoVR通过构建每个<查询，修改>对，关联多个有效目标视频，反映了实际任务的复杂性。为建模这些时间动态，提出了TF-CoVR-Base，一个简洁的两阶段训练框架，显著提升了检索性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有CoVR方法在细粒度视频检索中的不足，尤其是无法有效捕捉快速的时间变化和多目标视频的关联性。

**核心思路**：提出TF-CoVR基准，通过构建<查询，修改>对，利用大规模数据集中的多目标视频，增强了检索的实用性和灵活性。

**技术框架**：TF-CoVR-Base采用两阶段训练框架：第一阶段对视频编码器进行预训练，以获得时间上具有区分性的嵌入；第二阶段通过对比学习将构建的查询与候选视频进行对齐。

**关键创新**：TF-CoVR是首个专注于细粒度CoVR的大规模基准，能够处理多个有效目标视频的关联，显著提升了检索的准确性和实用性。

**关键设计**：在训练过程中，采用了对比学习损失函数，确保查询与候选视频之间的嵌入对齐，同时在视频编码器的设计上注重时间特征的提取。具体参数设置和网络结构细节在实验部分进行了详细描述。

## 📊 实验亮点

在TF-CoVR基准上，TF-CoVR-Base在零-shot情况下的mAP@50从5.92提升至7.51，经过微调后，状态-of-the-art性能从19.83提升至27.22，显示出显著的性能提升。

## 🎯 应用场景

该研究在体育视频分析、自动化视频摘要生成等领域具有广泛的应用潜力。通过提高细粒度视频检索的准确性，能够为运动员表现分析、赛事回放和观众体验提升提供支持，具有重要的实际价值和未来影响。

## 📄 摘要（原文）

> Composed Video Retrieval (CoVR) retrieves a target video given a query video and a modification text describing the intended change. Existing CoVR benchmarks emphasize appearance shifts or coarse event changes and therefore do not test the ability to capture subtle, fast-paced temporal differences. We introduce TF-CoVR, the first large-scale benchmark dedicated to temporally fine-grained CoVR. TF-CoVR focuses on gymnastics and diving, and provides 180K triplets drawn from FineGym and FineDiving datasets. Previous CoVR benchmarks, focusing on temporal aspect, link each query to a single target segment taken from the same video, limiting practical usefulness. In TF-CoVR, we instead construct each <query, modification> pair by prompting an LLM with the label differences between clips drawn from different videos; every pair is thus associated with multiple valid target videos (3.9 on average), reflecting real-world tasks such as sports-highlight generation. To model these temporal dynamics, we propose TF-CoVR-Base, a concise two-stage training framework: (i) pre-train a video encoder on fine-grained action classification to obtain temporally discriminative embeddings; (ii) align the composed query with candidate videos using contrastive learning. We conduct the first comprehensive study of image, video, and general multimodal embedding (GME) models on temporally fine-grained composed retrieval in both zero-shot and fine-tuning regimes. On TF-CoVR, TF-CoVR-Base improves zero-shot mAP@50 from 5.92 (LanguageBind) to 7.51, and after fine-tuning raises the state-of-the-art from 19.83 to 27.22.

