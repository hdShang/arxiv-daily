---
layout: default
title: ViBED-Net: Video Based Engagement Detection Network Using Face-Aware and Scene-Aware Spatiotemporal Cues
---

# ViBED-Net: Video Based Engagement Detection Network Using Face-Aware and Scene-Aware Spatiotemporal Cues

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2510.18016" class="toolbar-btn" target="_blank">📄 arXiv: 2510.18016v2</a>
  <a href="https://arxiv.org/pdf/2510.18016.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2510.18016v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2510.18016v2', 'ViBED-Net: Video Based Engagement Detection Network Using Face-Aware and Scene-Aware Spatiotemporal Cues')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Prateek Gothwal, Deeptimaan Banerjee, Ashis Kumer Biswas

**分类**: cs.CV, cs.LG

**发布日期**: 2025-10-20 (更新: 2025-10-24)

**备注**: 10 pages, 4 figures, 2 tables

**🔗 代码/项目**: [GITHUB](https://github.com/prateek-gothwal/ViBED-Net)

---

## 💡 一句话要点

**ViBED-Net：利用人脸和场景时空线索进行视频参与度检测**

🎯 **匹配领域**: **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `参与度检测` `在线学习` `人脸识别` `场景理解` `时空建模` `深度学习` `双流网络`

## 📋 核心要点

1. 现有在线学习参与度检测方法缺乏对学生面部表情和学习场景上下文的综合考虑，限制了检测精度。
2. ViBED-Net采用双流架构，分别处理人脸和场景信息，并利用LSTM和Transformer进行时序建模，融合多模态特征。
3. 在DAiSEE数据集上，ViBED-Net结合LSTM实现了73.43%的准确率，超越了现有技术水平，证明了方法的有效性。

## 📝 摘要（中文）

本文提出了一种名为ViBED-Net（基于视频的参与度检测网络）的深度学习框架，旨在通过双流架构从视频数据中评估学生的参与度，从而改进在线学习环境中的学生成果并实现个性化教学。ViBED-Net通过EfficientNetV2处理人脸裁剪和完整视频帧，以提取空间特征，从而捕获面部表情和完整场景上下文。然后，使用长短期记忆（LSTM）网络和Transformer编码器两种时间建模策略来分析这些特征随时间的变化。该模型在DAiSEE数据集上进行了评估，这是一个用于电子学习中情感状态识别的大规模基准。为了提高在代表性不足的参与度类别上的性能，我们应用了有针对性的数据增强技术。在测试的变体中，带有LSTM的ViBED-Net实现了73.43％的准确率，优于现有的最先进方法。ViBED-Net表明，结合人脸感知和场景感知的时空线索可以显着提高参与度检测的准确性。其模块化设计使其可以灵活地应用于教育、用户体验研究和内容个性化。这项工作通过为实际参与度分析提供可扩展的高性能解决方案，从而推进了基于视频的情感计算。

## 🔬 方法详解

**问题定义**：论文旨在解决在线学习环境中学生参与度检测的问题。现有方法通常只关注面部特征或场景信息，缺乏对两者之间关系的建模，导致检测精度不高，难以准确反映学生的真实参与状态。

**核心思路**：论文的核心思路是同时利用人脸感知和场景感知的时空线索进行参与度检测。通过双流网络分别提取人脸和场景的空间特征，然后利用时序模型捕捉特征随时间的变化，最后融合两种模态的信息进行预测。这种方法能够更全面地理解学生的参与状态。

**技术框架**：ViBED-Net采用双流架构，包含以下主要模块：1) 人脸流：使用人脸检测器提取人脸区域，然后使用EfficientNetV2提取人脸的空间特征。2) 场景流：直接使用EfficientNetV2提取完整视频帧的空间特征。3) 时序建模：分别使用LSTM网络和Transformer编码器对人脸和场景的时序特征进行建模。4) 融合与分类：将人脸和场景的时序特征进行融合，然后使用全连接层进行分类，预测学生的参与度。

**关键创新**：论文的关键创新在于：1) 提出了双流架构，同时考虑人脸和场景信息，更全面地理解学生的参与状态。2) 探索了LSTM和Transformer两种时序建模方法，并比较了它们在参与度检测任务中的性能。3) 针对数据集中类别不平衡的问题，采用了数据增强技术，提高了模型在少数类别上的性能。

**关键设计**：论文的关键设计包括：1) 使用EfficientNetV2作为空间特征提取器，因为它具有较高的效率和准确率。2) 尝试了LSTM和Transformer两种时序建模方法，并发现LSTM在DAiSEE数据集上表现更好。3) 采用了数据增强技术，包括旋转、缩放、平移等，以增加少数类别的样本数量。

## 📊 实验亮点

ViBED-Net在DAiSEE数据集上取得了显著的成果。其中，结合LSTM的ViBED-Net变体达到了73.43%的准确率，超越了现有的state-of-the-art方法。实验结果表明，同时考虑人脸和场景信息能够显著提高参与度检测的准确性。此外，数据增强技术也有效地提升了模型在少数类别上的性能。

## 🎯 应用场景

ViBED-Net可应用于在线教育平台，实时监测学生的参与度，为教师提供反馈，以便调整教学策略，提高教学效果。此外，该技术还可用于用户体验研究，分析用户在使用产品或服务时的参与度，从而优化产品设计。未来，该技术有望应用于内容个性化推荐，根据用户的参与度推荐更符合其兴趣的内容。

## 📄 摘要（原文）

> Engagement detection in online learning environments is vital for improving student outcomes and personalizing instruction. We present ViBED-Net (Video-Based Engagement Detection Network), a novel deep learning framework designed to assess student engagement from video data using a dual-stream architecture. ViBED-Net captures both facial expressions and full-scene context by processing facial crops and entire video frames through EfficientNetV2 for spatial feature extraction. These features are then analyzed over time using two temporal modeling strategies: Long Short-Term Memory (LSTM) networks and Transformer encoders. Our model is evaluated on the DAiSEE dataset, a large-scale benchmark for affective state recognition in e-learning. To enhance performance on underrepresented engagement classes, we apply targeted data augmentation techniques. Among the tested variants, ViBED-Net with LSTM achieves 73.43\% accuracy, outperforming existing state-of-the-art approaches. ViBED-Net demonstrates that combining face-aware and scene-aware spatiotemporal cues significantly improves engagement detection accuracy. Its modular design allows flexibility for application across education, user experience research, and content personalization. This work advances video-based affective computing by offering a scalable, high-performing solution for real-world engagement analysis. The source code for this project is available on https://github.com/prateek-gothwal/ViBED-Net .

