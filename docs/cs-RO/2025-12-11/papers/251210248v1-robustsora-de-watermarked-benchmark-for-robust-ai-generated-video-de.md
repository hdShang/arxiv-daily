---
layout: default
title: RobustSora: De-Watermarked Benchmark for Robust AI-Generated Video Detection
---

# RobustSora: De-Watermarked Benchmark for Robust AI-Generated Video Detection

**arXiv**: [2512.10248v1](https://arxiv.org/abs/2512.10248) | [PDF](https://arxiv.org/pdf/2512.10248.pdf)

**作者**: Zhuo Wang, Xiliang Liu, Ligang Sun

---

## 💡 一句话要点

**提出RobustSora基准以评估AI生成视频检测中水印鲁棒性的影响**

**关键词**: `AI生成视频检测` `水印鲁棒性` `基准评估` `Transformer模型` `多模态大语言模型` `虚假水印`

## 📋 核心要点

1. 核心问题：现有AI生成视频检测基准忽略数字水印对检测器性能的影响
2. 方法要点：构建包含真实与生成视频及水印变体的数据集，设计两个评估任务
3. 实验或效果：测试十种模型，发现水印操作导致性能变化2-8个百分点，揭示部分依赖

## 📄 摘要（原文）

> The proliferation of AI-generated video technologies poses challenges to information integrity. While recent benchmarks advance AIGC video detection, they overlook a critical factor: many state-of-the-art generative models embed digital watermarks in outputs, and detectors may partially rely on these patterns. To evaluate this influence, we present RobustSora, the benchmark designed to assess watermark robustness in AIGC video detection. We systematically construct a dataset of 6,500 videos comprising four types: Authentic-Clean (A-C), Authentic-Spoofed with fake watermarks (A-S), Generated-Watermarked (G-W), and Generated-DeWatermarked (G-DeW). Our benchmark introduces two evaluation tasks: Task-I tests performance on watermark-removed AI videos, while Task-II assesses false alarm rates on authentic videos with fake watermarks. Experiments with ten models spanning specialized AIGC detectors, transformer architectures, and MLLM approaches reveal performance variations of 2-8pp under watermark manipulation. Transformer-based models show consistent moderate dependency (6-8pp), while MLLMs exhibit diverse patterns (2-8pp). These findings indicate partial watermark dependency and highlight the need for watermark-aware training strategies. RobustSora provides essential tools to advance robust AIGC detection research.

