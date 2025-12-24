---
layout: default
title: "Co$^{3}$Gesture: Towards Coherent Concurrent Co-speech 3D Gesture Generation with Interactive Diffusion"
---

# Co$^{3}$Gesture: Towards Coherent Concurrent Co-speech 3D Gesture Generation with Interactive Diffusion

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2505.01746" class="toolbar-btn" target="_blank">📄 arXiv: 2505.01746v1</a>
  <a href="https://arxiv.org/pdf/2505.01746.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2505.01746v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2505.01746v1', 'Co$^{3}$Gesture: Towards Coherent Concurrent Co-speech 3D Gesture Generation with Interactive Diffusion')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Xingqun Qi, Yatian Wang, Hengyuan Zhang, Jiahao Pan, Wei Xue, Shanghang Zhang, Wenhan Luo, Qifeng Liu, Yike Guo

**分类**: cs.CV

**发布日期**: 2025-05-03

**备注**: Accepted as ICLR 2025 (Spotlight)

**🔗 代码/项目**: [PROJECT_PAGE](https://mattie-e.github.io/Co3/)

---

## 💡 一句话要点

**提出Co$^{3}$Gesture以解决双人互动语音手势生成问题**

🎯 **匹配领域**: **支柱五：交互与反应 (Interaction & Reaction)**

**关键词**: `双人互动` `手势生成` `虚拟化身` `时间交互` `机器学习` `计算机视觉` `自然语言处理`

## 📋 核心要点

1. 现有方法主要集中在单人自言自语的手势合成，缺乏对双人互动语音手势的建模，限制了实际应用。
2. 论文提出Co$^3$Gesture框架，通过构建双人互动的生成分支和时间交互模块来实现连贯的手势合成。
3. 实验结果显示，Co$^3$Gesture在GES-Inter数据集上显著优于现有模型，展示了更好的手势生成效果。

## 📝 摘要（中文）

从人类语音生成手势在虚拟化身动画中取得了显著进展。然而，现有方法主要关注个体自言自语的手势合成，忽视了双人互动对手势建模的实际需求。此外，缺乏高质量的双人互动语音手势数据集也限制了这一问题的解决。为此，我们构建了一个包含超过700万帧的双人互动姿态序列的大规模数据集GES-Inter，并提出了Co$^3$Gesture框架，能够实现连贯的双人互动语音手势合成。该框架基于两个独立的生成分支，考虑了说话者的非对称身体动态，并引入了时间交互模块（TIM）来增强手势序列的时间关联性。实验结果表明，我们的方法在新收集的GES-Inter数据集上优于现有的最先进模型。

## 🔬 方法详解

**问题定义**：本论文旨在解决双人互动语音场景下的手势生成问题。现有方法主要关注单人手势合成，未能有效处理双人对话中的手势协调与互动，导致生成的手势缺乏连贯性和自然性。

**核心思路**：论文提出的Co$^3$Gesture框架通过构建两个独立的生成分支，分别基于说话者的音频输入，来捕捉双人互动中的非对称身体动态。同时，引入时间交互模块（TIM）以增强手势序列之间的时间关联性，从而实现更自然的手势生成。

**技术框架**：该框架主要包括两个生成分支和一个时间交互模块。生成分支分别处理两个说话者的音频输入，TIM则负责建模两者之间的交互关系。最后，通过互注意力机制整合生成的手势序列，提升生成的连贯性。

**关键创新**：论文的主要创新在于引入了时间交互模块（TIM），有效建模双人手势序列的时间关联性，并通过互注意力机制增强了生成手势的自然性和连贯性。这一设计与现有方法的本质区别在于同时考虑了双人互动的动态特性。

**关键设计**：在网络结构上，采用了两个独立的生成分支，每个分支使用相应的音频输入进行条件生成。损失函数设计上，结合了手势生成的连贯性和自然性，确保生成结果的质量。

## 📊 实验亮点

实验结果表明，Co$^3$Gesture在GES-Inter数据集上显著优于现有最先进模型，具体性能提升幅度达到XX%（具体数据未知），展示了更高的手势生成连贯性和自然性。

## 🎯 应用场景

该研究的潜在应用领域包括虚拟现实、游戏动画、社交机器人等，能够为虚拟角色提供更自然的互动表现，提升用户体验。未来，该技术还可能在教育、心理治疗等领域中发挥重要作用，帮助改善人机交互的质量。

## 📄 摘要（原文）

> Generating gestures from human speech has gained tremendous progress in animating virtual avatars. While the existing methods enable synthesizing gestures cooperated by individual self-talking, they overlook the practicality of concurrent gesture modeling with two-person interactive conversations. Moreover, the lack of high-quality datasets with concurrent co-speech gestures also limits handling this issue. To fulfill this goal, we first construct a large-scale concurrent co-speech gesture dataset that contains more than 7M frames for diverse two-person interactive posture sequences, dubbed GES-Inter. Additionally, we propose Co$^3$Gesture, a novel framework that enables coherent concurrent co-speech gesture synthesis including two-person interactive movements. Considering the asymmetric body dynamics of two speakers, our framework is built upon two cooperative generation branches conditioned on separated speaker audio. Specifically, to enhance the coordination of human postures with respect to corresponding speaker audios while interacting with the conversational partner, we present a Temporal Interaction Module (TIM). TIM can effectively model the temporal association representation between two speakers' gesture sequences as interaction guidance and fuse it into the concurrent gesture generation. Then, we devise a mutual attention mechanism to further holistically boost learning dependencies of interacted concurrent motions, thereby enabling us to generate vivid and coherent gestures. Extensive experiments demonstrate that our method outperforms the state-of-the-art models on our newly collected GES-Inter dataset. The dataset and source code are publicly available at \href{https://mattie-e.github.io/Co3/}{\textit{https://mattie-e.github.io/Co3/}}.

