---
layout: default
title: "video-SALMONN 2: Caption-Enhanced Audio-Visual Large Language Models"
---

# video-SALMONN 2: Caption-Enhanced Audio-Visual Large Language Models

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.15220" class="toolbar-btn" target="_blank">📄 arXiv: 2506.15220v3</a>
  <a href="https://arxiv.org/pdf/2506.15220.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.15220v3" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.15220v3', 'video-SALMONN 2: Caption-Enhanced Audio-Visual Large Language Models')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Changli Tang, Yixuan Li, Yudong Yang, Jimin Zhuang, Guangzhi Sun, Wei Li, Zejun Ma, Chao Zhang

**分类**: cs.CV, cs.CL, cs.SD

**发布日期**: 2025-06-18 (更新: 2025-09-26)

**🔗 代码/项目**: [GITHUB](https://github.com/bytedance/video-SALMONN-2)

---

## 💡 一句话要点

**提出video-SALMONN 2以解决视频描述与问答问题**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音视频理解` `多轮优化` `字幕生成` `问答系统` `多模态学习`

## 📋 核心要点

1. 现有的音视频理解模型在视频描述和问答任务中存在准确性和细节不足的问题。
2. 论文提出的多轮直接偏好优化（MrDPO）方法，通过动态更新参考策略，提升了字幕的质量和准确性。
3. 在多个音视频理解基准测试中，3B和7B模型达到了SOTA结果，72B模型超越了所有其他开源系统。

## 📝 摘要（中文）

我们提出了video-SALMONN 2，这是一系列音视频大语言模型，在视频描述和问答（QA）任务中创造了新的最先进（SOTA）结果。我们的核心贡献是多轮直接偏好优化（MrDPO），结合了一个共同奖励完整性和事实准确性的字幕质量目标。与固定参考策略的标准DPO不同，MrDPO通过从最新偏好训练的轻量适配器中重新初始化参考，定期刷新参考，避免了参考过时的问题，促进了持续改进。该策略生成的字幕在细节和准确性上始终优于GPT-4o和Gemini-1.5 Pro等专有系统。我们进一步利用该模型生成高质量的视频字幕语料库，以便对新模型进行监督微调，超越了字幕生成的好处，在复杂视频问答任务上也表现出色。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有音视频理解模型在视频描述和问答任务中准确性不足的问题。现有方法往往依赖固定的参考策略，导致生成的字幕缺乏细节和准确性。

**核心思路**：论文提出的多轮直接偏好优化（MrDPO）方法，通过定期更新参考策略，避免了参考过时的问题，从而提升了字幕的质量。该方法结合了字幕质量目标，奖励完整性和事实准确性。

**技术框架**：整体架构包括多个模块，首先是音视频数据的输入处理，然后是通过MrDPO进行偏好优化，最后生成高质量的字幕。模型的训练过程中，使用轻量适配器动态更新参考策略。

**关键创新**：最重要的技术创新点是MrDPO的引入，它与传统的固定参考策略DPO方法本质上不同，能够实现持续的性能提升。

**关键设计**：在技术细节上，模型使用了特定的损失函数来平衡完整性和准确性，同时在网络结构中引入了轻量适配器，以便于动态更新参考策略。

## 📊 实验亮点

在实验中，3B和7B模型在多个音视频理解基准测试（如Video-MME、WorldSense等）中达到了新的最先进结果，72B模型的性能超越了所有其他开源系统，展示了显著的提升幅度，尤其是在复杂视频问答任务上表现优异。

## 🎯 应用场景

该研究的潜在应用领域包括视频内容生成、智能问答系统和多模态信息检索等。通过提升视频理解的准确性和细节，video-SALMONN 2能够为教育、娱乐和信息服务等行业带来实际价值，未来可能推动更智能的多模态交互系统的发展。

## 📄 摘要（原文）

> We present video-SALMONN 2, a family of audio-visual large language models that set new state-of-the-art (SOTA) results in video description and question answering (QA). Our core contribution is multi-round direct preference optimisation (MrDPO), paired with a caption-quality objective that jointly rewards completeness and factual accuracy. Unlike standard DPO with a fixed reference policy, MrDPO periodically refreshes the reference by bootstrapping from a newly re-initialised lightweight adapter trained on the latest preferences, avoiding reference staleness and enabling continual improvement. This strategy produces captions that are consistently more detailed and accurate than those from proprietary systems such as GPT-4o and Gemini-1.5 Pro. We further distil these gains by using our model to generate a high-quality video-caption corpus for supervised fine-tuning of new models, transferring benefits beyond captioning to strong performance on complex video-QA tasks. Across widely used audio-visual and visual-only understanding benchmarks (including Video-MME, WorldSense, AVUT, Video-Holmes, DailyOmni, MLVU, and LVBench), our 3B and 7B models achieve SOTA results at comparable scales, while the 72B model surpasses all other open-source systems. Our source code, models, and data are released at \href{https://github.com/bytedance/video-SALMONN-2}{https://github.com/bytedance/video-SALMONN-2}.

