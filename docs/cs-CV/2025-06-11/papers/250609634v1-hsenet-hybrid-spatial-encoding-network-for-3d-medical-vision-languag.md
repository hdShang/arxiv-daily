---
layout: default
title: "HSENet: Hybrid Spatial Encoding Network for 3D Medical Vision-Language Understanding"
---

# HSENet: Hybrid Spatial Encoding Network for 3D Medical Vision-Language Understanding

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2506.09634" class="toolbar-btn" target="_blank">📄 arXiv: 2506.09634v1</a>
  <a href="https://arxiv.org/pdf/2506.09634.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2506.09634v1" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2506.09634v1', 'HSENet: Hybrid Spatial Encoding Network for 3D Medical Vision-Language Understanding')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Yanzhao Shi, Xiaodan Zhang, Junzhong Ji, Haoning Jiang, Chengxin Zheng, Yinong Wang, Liangqiong Qu

**分类**: cs.CV, cs.AI

**发布日期**: 2025-06-11

**备注**: 27 pages, 9 figures. arXiv admin note: text overlap with arXiv:2410.14200 by other authors

**🔗 代码/项目**: [GITHUB](https://github.com/YanzhaoShi/HSENet)

---

## 💡 一句话要点

**提出HSENet以解决3D医学图像理解中的语言-视觉融合问题**

🎯 **匹配领域**: **支柱九：具身大模型 (Embodied Foundation Models)**

**关键词**: `3D医学图像` `语言-视觉理解` `多模态学习` `深度学习` `医学报告生成` `视觉问答` `空间编码` `模型对齐`

## 📋 核心要点

1. 现有方法主要集中于2D医学图像，无法有效捕捉复杂的3D解剖结构，导致误诊和诊断幻觉。
2. HSENet通过双3D视觉编码器和空间打包器，增强了对3D医学视觉线索的感知和投影能力，提升语言-视觉理解的准确性。
3. 实验结果显示，HSENet在3D语言-视觉检索、医学报告生成和视觉问答任务中均取得了显著性能提升，验证了其有效性。

## 📝 摘要（中文）

自动化的3D CT诊断能够提升临床医生的决策效率和准确性。然而，现有的多模态大语言模型主要集中于2D医学图像，限制了其对复杂3D解剖结构的理解，导致对细微病变的误解和诊断幻觉。为此，本文提出了混合空间编码网络（HSENet），通过有效的视觉感知和投影技术，利用丰富的3D医学视觉线索实现准确的语言-视觉理解。HSENet采用双3D视觉编码器，感知全局体积上下文和细粒度解剖细节，并通过双阶段对齐进行预训练。此外，提出的空间打包器通过基于质心的压缩，将高分辨率的3D空间区域浓缩为紧凑的信息视觉标记。实验结果表明，HSENet在3D语言-视觉检索、医学报告生成和视觉问答等任务中均取得了领先的性能。

## 🔬 方法详解

**问题定义**：本文旨在解决现有多模态大语言模型在3D医学图像理解中的不足，特别是对复杂3D解剖结构的捕捉能力不足，导致的误诊和幻觉问题。

**核心思路**：HSENet通过引入双3D视觉编码器来同时感知全局体积上下文和细粒度解剖细节，结合空间打包器有效压缩信息，从而实现更准确的语言-视觉理解。

**技术框架**：HSENet的整体架构包括双3D视觉编码器和空间打包器。双3D视觉编码器负责提取3D医学图像的特征，而空间打包器则将这些特征压缩为信息丰富的视觉标记，便于后续的语言生成。

**关键创新**：HSENet的主要创新在于双3D视觉编码器的设计和空间打包器的引入，使得模型能够有效处理3D医学图像，克服了传统方法对2D图像的依赖。

**关键设计**：在模型设计中，采用了双阶段对齐策略进行预训练，以确保编码器能够准确理解医学报告的语义。同时，空间打包器使用质心压缩方法，优化了信息的传递效率。

## 📊 实验亮点

实验结果表明，HSENet在3D语言-视觉检索任务中达到了39.85%的R@100，较基线提升了5.96%；在3D医学报告生成中，BLEU-4得分为24.01%，提升了8.01%；在3D视觉问答中，主要类别准确率达到了73.60%，提升了1.99%。

## 🎯 应用场景

该研究的潜在应用领域包括医学影像分析、临床辅助诊断和智能医疗系统。通过提升3D医学图像的语言-视觉理解能力，HSENet能够帮助医生更准确地进行疾病诊断，改善患者的治疗效果，未来可能在医疗行业产生深远的影响。

## 📄 摘要（原文）

> Automated 3D CT diagnosis empowers clinicians to make timely, evidence-based decisions by enhancing diagnostic accuracy and workflow efficiency. While multimodal large language models (MLLMs) exhibit promising performance in visual-language understanding, existing methods mainly focus on 2D medical images, which fundamentally limits their ability to capture complex 3D anatomical structures. This limitation often leads to misinterpretation of subtle pathologies and causes diagnostic hallucinations. In this paper, we present Hybrid Spatial Encoding Network (HSENet), a framework that exploits enriched 3D medical visual cues by effective visual perception and projection for accurate and robust vision-language understanding. Specifically, HSENet employs dual-3D vision encoders to perceive both global volumetric contexts and fine-grained anatomical details, which are pre-trained by dual-stage alignment with diagnostic reports. Furthermore, we propose Spatial Packer, an efficient multimodal projector that condenses high-resolution 3D spatial regions into a compact set of informative visual tokens via centroid-based compression. By assigning spatial packers with dual-3D vision encoders, HSENet can seamlessly perceive and transfer hybrid visual representations to LLM's semantic space, facilitating accurate diagnostic text generation. Experimental results demonstrate that our method achieves state-of-the-art performance in 3D language-visual retrieval (39.85% of R@100, +5.96% gain), 3D medical report generation (24.01% of BLEU-4, +8.01% gain), and 3D visual question answering (73.60% of Major Class Accuracy, +1.99% gain), confirming its effectiveness. Our code is available at https://github.com/YanzhaoShi/HSENet.

