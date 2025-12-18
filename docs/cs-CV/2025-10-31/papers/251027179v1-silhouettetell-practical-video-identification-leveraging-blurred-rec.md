---
layout: default
title: SilhouetteTell: Practical Video Identification Leveraging Blurred Recordings of Video Subtitles
---

# SilhouetteTell: Practical Video Identification Leveraging Blurred Recordings of Video Subtitles

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.27179" class="toolbar-btn" target="_blank">📄 arXiv: 2510.27179v1</a>
  <a href="https://arxiv.org/pdf/2510.27179.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.27179v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.27179v1', 'SilhouetteTell: Practical Video Identification Leveraging Blurred Recordings of Video Subtitles')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Guanchong Huang, Song Fang

**分类**: cs.CV, cs.CR

**发布日期**: 2025-10-31

**备注**: 16 pages, 29 figures. Accepted at 26th Privacy Enhancing Technologies Symposium (PETS 2026)

---

## 💡 一句话要点

**SilhouetteTell：利用模糊视频字幕记录实现视频识别攻击**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `视频识别` `隐私攻击` `字幕轮廓` `时空特征` `视频安全`

## 📋 核心要点

1. 现有视频识别技术依赖分析网络流量，易受加密和隐私保护措施影响，且难以应用于离线视频。
2. SilhouetteTell通过分析视频字幕轮廓的时空特征，建立与字幕文件的关联，从而实现视频识别。
3. 实验表明，SilhouetteTell在多种场景下均能有效识别视频，最远可在40米外进行攻击。

## 📝 摘要（中文）

视频识别攻击会严重威胁用户隐私，泄露用户的观看视频信息，进而暴露用户的兴趣爱好、宗教信仰、政治倾向、性取向和健康状况。视频观看历史可能被用于用户画像或广告投放，并可能导致网络欺凌、歧视或敲诈勒索。现有的视频推断技术通常依赖于分析在线视频流产生的网络流量。本文提出一种新的视频识别攻击方法SilhouetteTell，该方法结合了字幕轮廓的空间和时间域信息，构建字幕轮廓的时空特征。SilhouetteTell探索了视频录制字幕轮廓与其字幕文件之间的时空相关性，可以推断在线和离线视频。在现成智能手机上的综合实验证实了SilhouetteTell在各种设置下（包括远达40米的距离）推断视频标题和片段的高效性。

## 🔬 方法详解

**问题定义**：现有视频识别技术主要依赖于分析网络流量，这种方法对于加密流量或离线视频无能为力。此外，用户可以通过各种隐私保护措施来规避基于网络流量的识别。因此，需要一种不依赖网络流量，且能有效识别在线和离线视频的攻击方法。

**核心思路**：论文的核心思路是利用视频字幕的轮廓信息进行视频识别。字幕的内容决定了其在屏幕上的轮廓形状，并且连续字幕之间的时间差也蕴含了视频的信息。通过提取和分析字幕轮廓的时空特征，可以将其与已知的字幕文件进行匹配，从而识别出视频。这种方法不依赖于网络流量，因此可以应用于在线和离线视频。

**技术框架**：SilhouetteTell的整体框架包括以下几个主要阶段：1) 视频录制：使用智能手机等设备录制包含字幕的视频。2) 字幕轮廓提取：从录制的视频中提取字幕的轮廓图像。3) 时空特征构建：将字幕轮廓的空间信息和连续字幕之间的时间差结合起来，构建时空特征。4) 字幕文件匹配：将提取的时空特征与已知的字幕文件进行匹配，找到最匹配的字幕文件。5) 视频识别：根据匹配的字幕文件，识别出视频的标题和片段。

**关键创新**：SilhouetteTell的关键创新在于利用了字幕轮廓的时空特征进行视频识别。与传统的基于网络流量的视频识别方法相比，SilhouetteTell不依赖于网络流量，因此可以应用于在线和离线视频。此外，SilhouetteTell还结合了字幕轮廓的空间信息和时间信息，从而提高了视频识别的准确性。

**关键设计**：论文中没有详细说明具体的参数设置、损失函数或网络结构。但是，可以推断，字幕轮廓提取可能使用了图像处理技术，如边缘检测和轮廓提取算法。时空特征构建可能使用了时间序列分析方法，如动态时间规整（DTW）。字幕文件匹配可能使用了相似度度量方法，如余弦相似度或欧氏距离。

## 📊 实验亮点

SilhouetteTell在智能手机上进行了实验验证，结果表明该方法在各种设置下均能有效识别视频，包括在远达40米的距离下。这些实验结果表明，基于字幕轮廓的视频识别攻击具有很高的可行性和威胁性。

## 🎯 应用场景

SilhouetteTell的研究成果可应用于隐私安全领域，用于评估视频观看行为的隐私风险。同时，该技术也可能被恶意利用，例如用于未经授权的视频内容识别和追踪。因此，需要开发相应的防御机制，以保护用户的隐私。

## 📄 摘要（原文）

> Video identification attacks pose a significant privacy threat that can reveal videos that victims watch, which may disclose their hobbies, religious beliefs, political leanings, sexual orientation, and health status. Also, video watching history can be used for user profiling or advertising and may result in cyberbullying, discrimination, or blackmail. Existing extensive video inference techniques usually depend on analyzing network traffic generated by streaming online videos. In this work, we observe that the content of a subtitle determines its silhouette displayed on the screen, and identifying each subtitle silhouette also derives the temporal difference between two consecutive subtitles. We then propose SilhouetteTell, a novel video identification attack that combines the spatial and time domain information into a spatiotemporal feature of subtitle silhouettes. SilhouetteTell explores the spatiotemporal correlation between recorded subtitle silhouettes of a video and its subtitle file. It can infer both online and offline videos. Comprehensive experiments on off-the-shelf smartphones confirm the high efficacy of SilhouetteTell for inferring video titles and clips under various settings, including from a distance of up to 40 meters.

