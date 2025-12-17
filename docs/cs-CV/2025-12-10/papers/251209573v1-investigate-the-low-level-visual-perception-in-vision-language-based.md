---
layout: default
title: Investigate the Low-level Visual Perception in Vision-Language based Image Quality Assessment
---

# Investigate the Low-level Visual Perception in Vision-Language based Image Quality Assessment

**arXiv**: [2512.09573v1](https://arxiv.org/abs/2512.09573) | [PDF](https://arxiv.org/pdf/2512.09573.pdf)

**作者**: Yuan Li, Zitang Sun, Yen-Ju Chen, Shin'ya Nishida

---

## 💡 一句话要点

**提出低层失真感知任务以增强基于视觉语言模型的图像质量评估**

**关键词**: `图像质量评估` `多模态大语言模型` `低层视觉感知` `视觉语言对齐` `失真检测`

## 📋 核心要点

1. 核心问题：多模态大语言模型在图像质量评估中难以可靠检测低层失真，如模糊和噪声。
2. 方法要点：通过组件分析揭示视觉语言对齐阶段削弱低层特征，并引入视觉编码器专用约束。
3. 实验或效果：组件微调后，失真识别准确率从14.92%提升至84.43%，提高评估一致性。

## 📄 摘要（原文）

> Recent advances in Image Quality Assessment (IQA) have leveraged Multi-modal Large Language Models (MLLMs) to generate descriptive explanations. However, despite their strong visual perception modules, these models often fail to reliably detect basic low-level distortions such as blur, noise, and compression, and may produce inconsistent evaluations across repeated inferences. This raises an essential question: do MLLM-based IQA systems truly perceive the visual features that matter? To examine this issue, we introduce a low-level distortion perception task that requires models to classify specific distortion types. Our component-wise analysis shows that although MLLMs are structurally capable of representing such distortions, they tend to overfit training templates, leading to biases in quality scoring. As a result, critical low-level features are weakened or lost during the vision-language alignment transfer stage. Furthermore, by computing the semantic distance between visual features and corresponding semantic tokens before and after component-wise fine-tuning, we show that improving the alignment of the vision encoder dramatically enhances distortion recognition accuracy, increasing it from 14.92% to 84.43%. Overall, these findings indicate that incorporating dedicated constraints on the vision encoder can strengthen text-explainable visual representations and enable MLLM-based pipelines to produce more coherent and interpretable reasoning in vision-centric tasks.

