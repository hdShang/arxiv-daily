---
layout: default
title: TeleEgo: Benchmarking Egocentric AI Assistants in the Wild
---

# TeleEgo: Benchmarking Egocentric AI Assistants in the Wild

<div class="paper-toolbar">
  <div class="toolbar-left">
    <a href="https://arxiv.org/abs/2510.23981" target="_blank" class="toolbar-btn">arXiv: 2510.23981v4</a>
    <a href="https://arxiv.org/pdf/2510.23981.pdf" target="_blank" class="toolbar-btn">PDF</a>
  </div>
  <div class="toolbar-right">
    <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.23981v4" 
            onclick="toggleFavorite(this, '2510.23981v4', 'TeleEgo: Benchmarking Egocentric AI Assistants in the Wild')" title="收藏">
      ☆ 收藏
    </button>
    <button class="toolbar-btn share-btn" onclick="copyLink()" title="复制链接">
      🔗 分享
    </button>
  </div>
</div>


**作者**: Jiaqi Yan, Ruilong Ren, Jingren Liu, Shuning Xu, Ling Wang, Yiheng Wang, Xinlin Zhong, Yun Wang, Long Zhang, Xiangyu Chen, Changzhi Sun, Jixiang Luo, Dell Zhang, Hao Sun, Chi Zhang, Xuelong Li

**分类**: cs.CV

**发布日期**: 2025-10-28 (更新: 2025-12-10)

---

## 💡 一句话要点

**提出TeleEgo基准以评估现实场景中的自我中心AI助手**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `自我中心AI助手` `多模态输入` `长期记忆` `实时响应` `流媒体评估` `基准测试` `数据集构建` `智能助手`

## 📋 核心要点

1. 现有基准评估自我中心AI助手的能力时，通常缺乏现实的流媒体场景，且多模态输入的处理能力评估不够全面。
2. 论文提出TeleEgo基准，旨在通过长期流媒体数据评估自我中心AI助手的记忆、理解和推理能力，提供更真实的评估环境。
3. 实验结果表明，当前模型在RTA指标上表现出色，并通过MPT评估框架提供了对长期记忆的系统性研究基础。

## 📝 摘要（中文）

自我中心AI助手在现实环境中需要处理多模态输入（视频、音频、文本），实时响应并保持长期记忆。然而，现有基准通常孤立评估这些能力，缺乏现实的流媒体场景或仅支持短期任务。我们引入了TeleEgo，这是一个长期、流媒体的全模态基准，用于在真实日常环境中评估自我中心AI助手。该数据集包含每位参与者超过14小时的同步自我中心视频、音频和文本，涵盖工作与学习、生活与日常、社交活动和文化出游四个领域。所有数据在统一的全球时间线上对齐，并包括经过人工精炼的高质量视觉叙述和语音转录。TeleEgo定义了12个诊断子任务，涵盖记忆、理解和跨记忆推理三大核心能力，并提出了实时准确性（RTA）和记忆持久时间（MPT）作为评估指标。

## 🔬 方法详解

**问题定义**：本论文旨在解决现有自我中心AI助手评估基准在多模态输入、实时响应和长期记忆保持方面的不足，现有方法往往孤立评估这些能力，缺乏真实场景的支持。

**核心思路**：论文的核心思路是引入TeleEgo基准，通过提供长期、流媒体的全模态数据集，来全面评估自我中心AI助手在真实日常环境中的表现，特别是在记忆和理解方面的能力。

**技术框架**：TeleEgo数据集包含超过14小时的同步视频、音频和文本数据，涵盖四个领域，所有数据在统一时间线上对齐。基准定义了12个子任务，评估助手的记忆、理解和推理能力。

**关键创新**：最重要的技术创新点在于引入了实时准确性（RTA）和记忆持久时间（MPT）作为新的评估指标，前者关注在紧迫决策窗口下的正确性和响应性，后者则关注长期记忆的保持能力。

**关键设计**：在数据集构建中，采用了高质量的视觉叙述和语音转录，所有数据经过人工精炼，确保了数据的准确性和可靠性。

## 📊 实验亮点

实验结果显示，当前模型在实时准确性（RTA）评估中表现优异，能够在紧迫的决策环境中保持高水平的响应性。此外，MPT评估框架为长期记忆的研究提供了新的视角，推动了自我中心AI助手的系统性研究。

## 🎯 应用场景

该研究的潜在应用领域包括智能家居、个人助理、教育和社交机器人等，能够为自我中心AI助手的设计和优化提供重要的基准和评估标准。未来，TeleEgo基准将推动更强大的流媒体记忆能力的研究，促进自我中心AI助手在复杂环境中的应用。

## 📄 摘要（原文）

> Egocentric AI assistants in real-world settings must process multi-modal inputs (video, audio, text), respond in real time, and retain evolving long-term memory. However, existing benchmarks typically evaluate these abilities in isolation, lack realistic streaming scenarios, or support only short-term tasks. We introduce \textbf{TeleEgo}, a long-duration, streaming, omni-modal benchmark for evaluating egocentric AI assistants in realistic daily contexts. The dataset features over 14 hours per participant of synchronized egocentric video, audio, and text across four domains: work \& study, lifestyle \& routines, social activities, and outings \& culture. All data is aligned on a unified global timeline and includes high-quality visual narrations and speech transcripts, curated through human refinement.TeleEgo defines 12 diagnostic subtasks across three core capabilities: Memory (recalling past events), Understanding (interpreting the current moment), and Cross-Memory Reasoning (linking distant events). It contains 3,291 human-verified QA items spanning multiple question formats (single-choice, binary, multi-choice, and open-ended), evaluated strictly in a streaming setting. We propose Real-Time Accuracy (RTA) to jointly capture correctness and responsiveness under tight decision windows, and Memory Persistence Time (MPT) as a forward-looking metric for long-term retention in continuous streams. In this work, we report RTA results for current models and release TeleEgo, together with an MPT evaluation framework, as a realistic and extensible benchmark for future egocentric assistants with stronger streaming memory, enabling systematic study of both real-time behavior and long-horizon memory.

