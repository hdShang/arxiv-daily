---
layout: default
title: Seedance 1.5 pro: A Native Audio-Visual Joint Generation Foundation Model
---

# Seedance 1.5 pro: A Native Audio-Visual Joint Generation Foundation Model

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2512.13507" class="toolbar-btn" target="_blank">📄 arXiv: 2512.13507</a>
  <a href="https://arxiv.org/pdf/2512.13507.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2512.13507" onclick="toggleFavorite(this, '2512.13507', 'Seedance 1.5 pro: A Native Audio-Visual Joint Generation Foundation Model')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Heyi Chen, Siyan Chen, Xin Chen, Yanfei Chen, Ying Chen, Zhuo Chen, Feng Cheng, Tianheng Cheng, Xinqi Cheng, Xuyan Chi, Jian Cong, Jing Cui, Qinpeng Cui, Qide Dong, Junliang Fan, Jing Fang, Zetao Fang, Chengjian Feng, Han Feng, Mingyuan Gao, Yu Gao, Dong Guo, Qiushan Guo, Boyang Hao, Qingkai Hao, Bibo He, Qian He, Tuyen Hoang, Ruoqing Hu, Xi Hu, Weilin Huang, Zhaoyang Huang, Zhongyi Huang, Donglei Ji, Siqi Jiang, Wei Jiang, Yunpu Jiang, Zhuo Jiang, Ashley Kim, Jianan Kong, Zhichao Lai, Shanshan Lao, Yichong Leng, Ai Li, Feiya Li, Gen Li, Huixia Li, JiaShi Li, Liang Li, Ming Li, Shanshan Li, Tao Li, Xian Li, Xiaojie Li, Xiaoyang Li, Xingxing Li, Yameng Li, Yifu Li, Yiying Li, Chao Liang, Han Liang, Jianzhong Liang, Ying Liang, Zhiqiang Liang, Wang Liao, Yalin Liao, Heng Lin, Kengyu Lin, Shanchuan Lin, Xi Lin, Zhijie Lin, Feng Ling, Fangfang Liu, Gaohong Liu, Jiawei Liu, Jie Liu, Jihao Liu, Shouda Liu, Shu Liu, Sichao Liu, Songwei Liu, Xin Liu, Xue Liu, Yibo Liu, Zikun Liu, Zuxi Liu, Junlin Lyu, Lecheng Lyu, Qian Lyu, Han Mu, Xiaonan Nie, Jingzhe Ning, Xitong Pan, Yanghua Peng, Lianke Qin, Xueqiong Qu, Yuxi Ren, Kai Shen, Guang Shi, Lei Shi

**分类**: cs.CV

**发布日期**: 2025-12-18

---

## 💡 一句话要点

**Seedance 1.5 pro：原生音视频联合生成基础模型，提升专业级内容创作能力**

🎯 **匹配领域**: **支柱二：RL算法与架构 (RL & Architecture)** **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `音视频生成` `扩散模型` `Transformer` `跨模态学习` `唇形同步`

## 📋 核心要点

1. 现有视频生成方法在音视频同步和生成质量方面存在挑战，难以满足专业级内容创作的需求。
2. Seedance 1.5 pro采用双分支扩散Transformer架构，结合跨模态联合模块和多阶段数据管道，实现高质量音视频同步生成。
3. 通过监督微调、强化学习等后训练优化，以及推理加速框架，显著提升了生成质量和效率，并具备多语言唇形同步能力。

## 📝 摘要（中文）

本文介绍了Seedance 1.5 pro，一个专为原生、联合音视频生成而设计的基石模型。该模型采用双分支扩散Transformer架构，集成了一个跨模态联合模块和一个专门的多阶段数据管道，实现了卓越的音视频同步和卓越的生成质量。为了确保实际应用价值，我们实施了细致的后训练优化，包括基于高质量数据集的监督微调（SFT）和利用多维奖励模型的人工反馈强化学习（RLHF）。此外，我们还引入了一个加速框架，将推理速度提高了10倍以上。Seedance 1.5 pro以其精确的多语言和方言唇形同步、动态电影摄像机控制和增强的叙事连贯性而著称，使其成为专业级内容创作的强大引擎。Seedance 1.5 pro现已在火山引擎上提供。

## 🔬 方法详解

**问题定义**：当前音视频生成模型在生成高质量、同步性好的内容方面存在挑战，尤其是在多语言唇形同步、动态镜头控制和叙事连贯性方面表现不足。现有方法难以满足专业级内容创作的需求，需要更强大的基础模型来解决这些问题。

**核心思路**：Seedance 1.5 pro的核心思路是构建一个原生、联合的音视频生成基础模型，通过深度融合音频和视频信息，实现高质量的同步生成。模型采用双分支架构，分别处理音频和视频信息，并通过跨模态联合模块实现信息融合。此外，通过多阶段数据管道和后训练优化，进一步提升生成质量和实用性。

**技术框架**：Seedance 1.5 pro采用双分支扩散Transformer架构。该架构包含两个主要分支：音频分支和视频分支。音频分支处理音频信息，视频分支处理视频信息。两个分支通过一个跨模态联合模块进行信息融合。模型还包含一个多阶段数据管道，用于处理不同类型的数据。后训练优化包括监督微调（SFT）和人工反馈强化学习（RLHF）。此外，还引入了一个加速框架，用于提高推理速度。

**关键创新**：Seedance 1.5 pro的关键创新在于其原生、联合的音视频生成方法，以及双分支扩散Transformer架构和跨模态联合模块。该模型能够实现高质量的音视频同步生成，并具备多语言唇形同步、动态电影摄像机控制和增强的叙事连贯性。此外，后训练优化和加速框架进一步提升了模型的实用性。

**关键设计**：模型的关键设计包括：1) 双分支扩散Transformer架构，用于分别处理音频和视频信息；2) 跨模态联合模块，用于实现音频和视频信息的融合；3) 多阶段数据管道，用于处理不同类型的数据；4) 监督微调（SFT），用于提升生成质量；5) 人工反馈强化学习（RLHF），用于优化生成结果；6) 推理加速框架，用于提高推理速度。具体的参数设置、损失函数和网络结构等细节未在摘要中详细说明，属于未知信息。

## 📊 实验亮点

摘要中提到，Seedance 1.5 pro实现了卓越的音视频同步和卓越的生成质量。通过后训练优化，包括监督微调（SFT）和人工反馈强化学习（RLHF），进一步提升了生成质量。此外，引入的加速框架将推理速度提高了10倍以上。该模型还具备精确的多语言和方言唇形同步、动态电影摄像机控制和增强的叙事连贯性。

## 🎯 应用场景

Seedance 1.5 pro可广泛应用于电影制作、游戏开发、广告创意、虚拟现实等领域。它能够帮助专业人士和普通用户快速生成高质量的音视频内容，降低创作门槛，提升创作效率。未来，该模型有望成为内容创作领域的重要基础设施，推动音视频生成技术的进一步发展。

## 📄 摘要（原文）

> Recent strides in video generation have paved the way for unified audio-visual generation. In this work, we present Seedance 1.5 pro, a foundational model engineered specifically for native, joint audio-video generation. Leveraging a dual-branch Diffusion Transformer architecture, the model integrates a cross-modal joint module with a specialized multi-stage data pipeline, achieving exceptional audio-visual synchronization and superior generation quality. To ensure practical utility, we implement meticulous post-training optimizations, including Supervised Fine-Tuning (SFT) on high-quality datasets and Reinforcement Learning from Human Feedback (RLHF) with multi-dimensional reward models. Furthermore, we introduce an acceleration framework that boosts inference speed by over 10X. Seedance 1.5 pro distinguishes itself through precise multilingual and dialect lip-syncing, dynamic cinematic camera control, and enhanced narrative coherence, positioning it as a robust engine for professional-grade content creation. Seedance 1.5 pro is now accessible on Volcano Engine atthis https URL.

