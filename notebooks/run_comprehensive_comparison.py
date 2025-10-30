#!/usr/bin/env python3
"""
Comprehensive ML vs Statistical Models Comparison Runner

This is the main script that runs comprehensive comparisons across all problem types,
datasets, and models, providing detailed analysis and reporting.

Usage:
    python run_comprehensive_comparison.py [options]

Examples:
    # Run all comparisons
    python run_comprehensive_comparison.py

    # Run specific problem types
    python run_comprehensive_comparison.py --problem-types regression classification

    # Run specific datasets
    python run_comprehensive_comparison.py --datasets california_housing iris

    # Run specific models
    python run_comprehensive_comparison.py --models linear_regression ols_regression

    # Generate report only
    python run_comprehensive_comparison.py --report-only

Author: ML vs Statistical Models Framework
Version: 2.0.0
"""

import warnings
import sys
import os
import argparse
import logging

# Suppress all warnings
warnings.filterwarnings('ignore')
from pathlib import Path
from datetime import datetime

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.analysis.comprehensive_comparison import ComprehensiveComparisonFramework
from src.core import Config

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('comprehensive_comparison.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def main():
    """Main function to run comprehensive comparison."""
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description='Comprehensive ML vs Statistical Models Comparison',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_comprehensive_comparison.py
  python run_comprehensive_comparison.py --problem-types regression classification
  python run_comprehensive_comparison.py --datasets california_housing iris
  python run_comprehensive_comparison.py --models linear_regression ols_regression
  python run_comprehensive_comparison.py --report-only
        """
    )
    
    parser.add_argument(
        '--problem-types',
        nargs='+',
        choices=['regression', 'classification', 'time_series', 'survival_analysis'],
        help='Problem types to compare (default: all)'
    )
    
    parser.add_argument(
        '--datasets',
        nargs='+',
        help='Specific datasets to use (default: all for each problem type)'
    )
    
    parser.add_argument(
        '--models',
        nargs='+',
        help='Specific models to compare (default: all for each problem type)'
    )
    
    parser.add_argument(
        '--report-only',
        action='store_true',
        help='Generate report from existing results only'
    )
    
    parser.add_argument(
        '--output-dir',
        default='comprehensive_results',
        help='Output directory for results (default: comprehensive_results)'
    )
    
    parser.add_argument(
        '--config',
        help='Path to configuration file'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging and detailed output'
    )
    
    parser.add_argument(
        '--detailed-metrics',
        action='store_true',
        help='Print detailed metrics for each model'
    )
    
    args = parser.parse_args()
    
    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Initialize configuration
    config = Config(args.config) if args.config else Config()
    
    # Initialize framework
    framework = ComprehensiveComparisonFramework(config)
    
    print("=" * 80)
    print("COMPREHENSIVE ML vs STATISTICAL MODELS COMPARISON")
    print("=" * 80)
    print(f"Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    try:
        if args.report_only:
            # Generate report from existing results
            print("Generating report from existing results...")
            report = framework.generate_comprehensive_report()
            print(report)
            
            # Save report
            output_dir = Path(args.output_dir)
            output_dir.mkdir(exist_ok=True)
            
            report_file = output_dir / f"comprehensive_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(report_file, 'w') as f:
                f.write(report)
            
            print(f"\nReport saved to: {report_file}")
            
        else:
            # Run comprehensive comparison
            print("Running comprehensive comparison...")
            print()
            
            # Display configuration
            print("CONFIGURATION:")
            print("-" * 20)
            if args.problem_types:
                print(f"Problem types: {', '.join(args.problem_types)}")
            else:
                print("Problem types: All available")
            
            if args.datasets:
                print(f"Datasets: {', '.join(args.datasets)}")
            else:
                print("Datasets: All available for each problem type")
            
            if args.models:
                print(f"Models: {', '.join(args.models)}")
            else:
                print("Models: All available for each problem type")
            
            print(f"Output directory: {args.output_dir}")
            print()
            
            # Run comparison
            try:
                results = framework.run_comprehensive_comparison(
                    problem_types=args.problem_types,
                    datasets=args.datasets,
                    models=args.models,
                    save_results=True
                )
            except Exception as e:
                logger.error(f"Error during comparison: {e}")
                print(f"❌ Error: {e}")
                return 1
            
            # Generate and display report
            print("\n" + "=" * 80)
            print("GENERATING COMPREHENSIVE REPORT")
            print("=" * 80)
            
            try:
                report = framework.generate_comprehensive_report()
                print(report)
            except Exception as e:
                logger.error(f"Error generating report: {e}")
                print(f"❌ Error generating report: {e}")
                return 1
            
            # Save report
            output_dir = Path(args.output_dir)
            output_dir.mkdir(exist_ok=True)
            
            report_file = output_dir / f"comprehensive_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            with open(report_file, 'w') as f:
                f.write(report)
            
            print(f"\nReport saved to: {report_file}")
            
            # Display key insights
            print("\n" + "=" * 80)
            print("KEY INSIGHTS")
            print("=" * 80)
            
            if 'recommendations' in results:
                recommendations = results['recommendations']
                
                if 'best_for_speed' in recommendations and recommendations['best_for_speed']:
                    best_speed = recommendations['best_for_speed']
                    print(f"🚀 FASTEST MODEL: {best_speed['model_name']} ({best_speed['model_category']})")
                    print(f"   Training time: {best_speed['training_time']:.4f}s")
                
                if 'best_for_interpretability' in recommendations and recommendations['best_for_interpretability']:
                    best_interp = recommendations['best_for_interpretability']
                    print(f"🧠 MOST INTERPRETABLE: {best_interp['model_name']} ({best_interp['model_category']})")
                    print(f"   Explainability score: {best_interp['explainability_score']}/100")
                
                if 'best_for_production' in recommendations and recommendations['best_for_production']:
                    best_prod = recommendations['best_for_production']
                    print(f"🏭 BEST FOR PRODUCTION: {best_prod['model_name']} ({best_prod['model_category']})")
                    print(f"   Production score: {best_prod['production_score']:.4f}")
                
                if 'best_for_research' in recommendations and recommendations['best_for_research']:
                    best_research = recommendations['best_for_research']
                    print(f"🔬 BEST FOR RESEARCH: {best_research['model_name']} ({best_research['model_category']})")
                    print(f"   Explainability score: {best_research['explainability_score']}/100")
            
            print("\n" + "=" * 80)
            print("COMPARISON COMPLETE!")
            print("=" * 80)
            print(f"Results saved to: {args.output_dir}/")
            print(f"Log file: comprehensive_comparison.log")
            print(f"Completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    except KeyboardInterrupt:
        print("\n\nComparison interrupted by user.")
        return 1
    
    except Exception as e:
        logger.error(f"Error during comparison: {e}")
        print(f"\n❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
