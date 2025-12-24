---
layout: default
title: "3-Tracer: A Tri-level Temporal-Aware Framework for Audio Forgery Detection and Localization"
---

# 3-Tracer: A Tri-level Temporal-Aware Framework for Audio Forgery Detection and Localization

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2511.21237" class="toolbar-btn" target="_blank">📄 arXiv: 2511.21237v2</a>
  <a href="https://arxiv.org/pdf/2511.21237.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2511.21237v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2511.21237v2', '3-Tracer: A Tri-level Temporal-Aware Framework for Audio Forgery Detection and Localization')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Shuhan Xia, Xuannan Liu, Xing Cui, Peipei Li

**分类**: cs.CV

**发布日期**: 2025-11-26 (更新: 2025-12-01)

**备注**: The experimental results in this paper have been further improved and updated; the baseline results do not match existing results, therefore the paper needs to be retracted

---

## 💡 一句话要点

**提出T3-Tracer，用于音频篡改检测与定位，实现帧、段、音频三层时序分析。**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱三：空间感知 (Perception & SLAM)**

**关键词**: `音频篡改检测` `时序分析` `多尺度学习` `深度学习` `音频取证`

## 📋 核心要点

1. 现有音频篡改检测方法缺乏对音频数据多层次时序信息的有效利用，难以检测语义关键帧的部分篡改。
2. T3-Tracer框架通过帧-音频特征聚合和段级多尺度差异感知，实现帧、段、音频三个层次的联合分析，从而检测篡改痕迹。
3. 实验结果表明，T3-Tracer在三个具有挑战性的数据集上均取得了优于现有技术水平的性能表现。

## 📝 摘要（中文）

本文提出了一种新的音频篡改检测框架T3-Tracer，旨在解决部分音频篡改问题。该问题中，攻击者选择性地修改部分但语义上关键的帧，同时保持整体感知真实性，使得检测极具挑战。现有方法侧重于独立检测单个帧是否被篡改，缺乏捕获不同时间尺度上瞬时和持续异常的层次结构。T3-Tracer通过在帧、段和音频三个层面上联合分析音频，全面检测篡改痕迹。该框架包含两个互补的核心模块：帧-音频特征聚合模块（FA-FAM）和段级多尺度差异感知模块（SMDAM）。FA-FAM用于检测每个音频帧的真伪，结合帧级和音频级的时间信息，检测帧内篡改线索和全局语义不一致性。SMDAM通过在多尺度时间窗口上联合建模帧特征和帧间差异，检测篡改边界上的突变异常，从而细化和纠正帧检测。在三个具有挑战性的数据集上进行的大量实验表明，该方法达到了最先进的性能。

## 🔬 方法详解

**问题定义**：当前音频篡改检测面临的挑战是，攻击者可以巧妙地篡改音频中的部分关键帧，同时保持音频整体的听觉真实性。现有的方法主要集中在独立检测单个帧的真伪，忽略了音频数据内在的时序结构，以及不同时间尺度上的篡改痕迹，导致检测精度不高。

**核心思路**：T3-Tracer的核心思路是利用音频数据在帧、段和音频三个层次上的时序信息，构建一个多层次的分析框架。通过在不同时间尺度上检测篡改痕迹，可以更全面地识别音频中的异常，提高篡改检测的准确性。该方法旨在捕捉局部帧级别的篡改线索，以及全局音频级别的语义不一致性。

**技术框架**：T3-Tracer框架包含两个主要模块：帧-音频特征聚合模块（FA-FAM）和段级多尺度差异感知模块（SMDAM）。FA-FAM首先提取帧级别和音频级别的特征，然后将它们聚合起来，用于检测每个音频帧的真伪。SMDAM则在段级别上分析音频数据，通过多尺度的时间窗口来检测篡改边界上的突变异常，从而细化和纠正帧级别的检测结果。整体流程是从局部到全局，再从全局到局部的迭代优化过程。

**关键创新**：T3-Tracer的关键创新在于其三层时序分析框架，能够同时考虑帧级别、段级别和音频级别的时序信息。FA-FAM模块通过聚合帧级别和音频级别的特征，可以有效地检测帧内的篡改线索和全局的语义不一致性。SMDAM模块则通过多尺度的时间窗口来检测篡改边界上的突变异常，从而提高检测的准确性。这种多层次的分析方法是现有方法所缺乏的。

**关键设计**：FA-FAM模块的具体实现细节未知，但可以推测其可能使用了注意力机制或者其他特征融合方法来聚合帧级别和音频级别的特征。SMDAM模块的关键设计在于多尺度时间窗口的选择，不同的时间窗口可以捕捉不同时间尺度上的篡改痕迹。损失函数的设计也至关重要，需要能够有效地衡量篡改的程度，并指导模型的训练。

## 📊 实验亮点

T3-Tracer在三个具有挑战性的音频篡改数据集上进行了评估，实验结果表明，该方法在篡改检测和定位方面均取得了最先进的性能。具体的性能数据和提升幅度在论文中给出，相较于现有方法，T3-Tracer能够更准确地检测和定位音频篡改区域。

## 🎯 应用场景

该研究成果可应用于数字取证、新闻媒体真实性验证、智能语音助手安全等领域。通过检测音频篡改，可以防止虚假信息的传播，维护社会诚信，保障用户安全。未来，该技术可进一步扩展到视频等多媒体内容的篡改检测，具有广阔的应用前景。

## 📄 摘要（原文）

> Recently, partial audio forgery has emerged as a new form of audio manipulation. Attackers selectively modify partial but semantically critical frames while preserving the overall perceptual authenticity, making such forgeries particularly difficult to detect. Existing methods focus on independently detecting whether a single frame is forged, lacking the hierarchical structure to capture both transient and sustained anomalies across different temporal levels. To address these limitations, We identify three key levels relevant to partial audio forgery detection and present T3-Tracer, the first framework that jointly analyzes audio at the frame, segment, and audio levels to comprehensively detect forgery traces. T3-Tracer consists of two complementary core modules: the Frame-Audio Feature Aggregation Module (FA-FAM) and the Segment-level Multi-Scale Discrepancy-Aware Module (SMDAM). FA-FAM is designed to detect the authenticity of each audio frame. It combines both frame-level and audio-level temporal information to detect intra-frame forgery cues and global semantic inconsistencies. To further refine and correct frame detection, we introduce SMDAM to detect forgery boundaries at the segment level. It adopts a dual-branch architecture that jointly models frame features and inter-frame differences across multi-scale temporal windows, effectively identifying abrupt anomalies that appeared on the forged boundaries. Extensive experiments conducted on three challenging datasets demonstrate that our approach achieves state-of-the-art performance.

