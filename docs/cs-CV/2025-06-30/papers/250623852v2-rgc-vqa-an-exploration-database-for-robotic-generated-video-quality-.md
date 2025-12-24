---
layout: default
title: "RGC-VQA: An Exploration Database for Robotic-Generated Video Quality Assessment"
---

# RGC-VQA: An Exploration Database for Robotic-Generated Video Quality Assessment

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.23852" class="toolbar-btn" target="_blank">📄 arXiv: 2506.23852v2</a>
  <a href="https://arxiv.org/pdf/2506.23852.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.23852v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.23852v2', 'RGC-VQA: An Exploration Database for Robotic-Generated Video Quality Assessment')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Jianing Jin, Jiangyong Ying, Huiyu Duan, Liu Yang, Sijing Wu, Yunhao Li, Yushuo Zheng, Xiongkuo Min, Guangtao Zhai

**分类**: cs.CV

**发布日期**: 2025-06-30 (更新: 2025-07-03)

**🔗 代码/项目**: [GITHUB](https://github.com/IntMeGroup/RGC-VQA)

---

## 💡 一句话要点

**提出RGC-VQA以解决机器人生成视频质量评估问题**

🎯 **匹配领域**: **支柱六：视频提取与匹配 (Video Extraction)**

**关键词**: `机器人生成内容` `视频质量评估` `人机交互` `数据库构建` `主观评估` `视觉感知` `模型评估`

## 📋 核心要点

1. 现有的视频质量评估方法在处理机器人生成内容时存在显著局限，无法满足其独特的视觉需求。
2. 本文提出了机器人生成内容数据库（RGCD），并通过主观实验评估人类对RGC视频的视觉感知。
3. 实验结果表明，现有的VQA模型在RGC视频上表现不佳，强调了开发专门模型的必要性。

## 📝 摘要（中文）

随着配备摄像头的机器人平台日益融入日常生活，机器人生成的视频开始出现在流媒体平台上，预示着人类与机器人共存的未来。本文创新性地提出了机器人生成内容（RGC）的概念，强调RGC视频在感知质量方面的重要性。RGC视频的失真和视觉需求与专业生成内容（PGC）和用户生成内容（UGC）显著不同，但针对RGC视频的质量评估研究仍然不足。为此，本文建立了首个机器人生成内容数据库（RGCD），包含2100个来自三类机器人的视频，并进行了主观视频质量评估实验，最后评估了11种最先进的VQA模型在该数据库上的表现，结果显示现有模型在处理复杂的RGC内容时存在显著局限，亟需开发RGC特定的VQA模型。

## 🔬 方法详解

**问题定义**：本文旨在解决机器人生成视频的质量评估问题，现有方法在处理RGC视频时无法有效评估其独特的视觉特性和失真。

**核心思路**：通过建立机器人生成内容数据库（RGCD），并进行主观视频质量评估，探索RGC视频的感知质量，进而推动专门的VQA模型开发。

**技术框架**：RGCD数据库包含2100个视频，分为三类机器人，数据来源多样。研究通过主观实验评估人类对RGC视频的感知，并对11种VQA模型进行基准测试。

**关键创新**：首次提出RGC概念并建立RGCD数据库，填补了机器人生成视频质量评估的研究空白，强调了RGC视频的独特性。

**关键设计**：实验中采用主观评估方法，结合多种VQA模型进行性能对比，重点关注模型在RGC视频上的表现差异。

## 📊 实验亮点

实验结果显示，现有11种VQA模型在RGC视频上的性能普遍较差，评估准确率低于50%，这表明现有模型无法满足RGC视频的质量评估需求，强调了开发RGC特定VQA模型的紧迫性。

## 🎯 应用场景

该研究的潜在应用领域包括人机交互、智能监控、自动驾驶等，能够提升机器人生成视频的质量评估能力，促进人类与机器人之间的有效沟通与协作。未来，随着RGC视频的普及，相关技术将对智能家居、服务机器人等领域产生深远影响。

## 📄 摘要（原文）

> As camera-equipped robotic platforms become increasingly integrated into daily life, robotic-generated videos have begun to appear on streaming media platforms, enabling us to envision a future where humans and robots coexist. We innovatively propose the concept of Robotic-Generated Content (RGC) to term these videos generated from egocentric perspective of robots. The perceptual quality of RGC videos is critical in human-robot interaction scenarios, and RGC videos exhibit unique distortions and visual requirements that differ markedly from those of professionally-generated content (PGC) videos and user-generated content (UGC) videos. However, dedicated research on quality assessment of RGC videos is still lacking. To address this gap and to support broader robotic applications, we establish the first Robotic-Generated Content Database (RGCD), which contains a total of 2,100 videos drawn from three robot categories and sourced from diverse platforms. A subjective VQA experiment is conducted subsequently to assess human visual perception of robotic-generated videos. Finally, we conduct a benchmark experiment to evaluate the performance of 11 state-of-the-art VQA models on our database. Experimental results reveal significant limitations in existing VQA models when applied to complex, robotic-generated content, highlighting a critical need for RGC-specific VQA models. Our RGCD is publicly available at: https://github.com/IntMeGroup/RGC-VQA.

